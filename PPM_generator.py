import numpy as np
import matplotlib.pyplot as plt


def char_to_binary(char):
    """
    Converts a character into its 8-bit ASCII binary representation.

    :param char: A single character of the name.
    :return: A string representing the 8-bit binary value of the ASCII character.
    """
    asc = ord(char)
    binary = bin(asc)
    binary = binary.lstrip('-0b')  # Remove unwanted prefix

    # Check the length and add '0's if needed to make it 8-bit
    s = 8 - len(binary)
    if s > 0:
        binary = s * '0' + binary
    return binary


def bit_to_symbol(bits, M):
    """
    Converts binary bits to their corresponding symbol in Gray code for a given M.

    :param bits: A string of bits.
    :param M: The modulation order.
    :return: An integer representing the symbol in Gray code.
    """
    # Gray code mappings for each M value
    Gray_2 = {'0': 0, '1': 1}
    Gray_4 = {'00': 0, '01': 1, '11': 2, '10': 3}
    Gray_8 = {'000': 0, '001': 1, '011': 2, '010': 3, '110': 4, '111': 5, '101': 6, '100': 7}
    Gray_16 = {'0000': 0, '0001': 1, '0011': 2, '0010': 3, '0110': 4, '0111': 5, '0101': 6, '0100': 7, '1100': 8,
               '1101': 9, '1111': 10, '1110': 11, '1010': 12, '1011': 13, '1001': 14, '1000': 15}

    if M == 2:
        return Gray_2[bits]
    elif M == 4:
        return Gray_4[bits]
    elif M == 8:
        return Gray_8[bits]
    elif M == 16:
        return Gray_16[bits]


def ppm_modulation(k, Ts, M, t_start):
    """
    Create the PPM signal for the k-th symbol.

    :param k: The symbol value in Gray code.
    :param Ts: The symbol duration.
    :param M: The modulation order.
    :param t_start: The start time of the symbol.
    :return: time: A numpy array representing the time samples and
    signal: A numpy array representing the PPM signal amplitude (0 or 1).
    """
    # Create time samples for the symbol duration
    time = np.linspace(t_start, t_start + Ts, M * 100)
    signal = np.zeros(len(time))

    # Set the signal to 1 for the duration of the k-th symbol's position
    for i in range(0, len(time)):
        if time[i] - t_start >= k * Ts / M and time[i] - t_start <= (k + 1) * Ts / M:
            signal[i] = 1

    return time, signal


def plot_ppm_signal(name, M_array):
    """
    Plot the PPM signal for a given name and array of M values.

    :param name: The name to encode in the PPM signal.
    :param M_array: An array of modulation orders (M values).
    """
    for M in M_array:
        n = int(np.log2(M))     # Number of bits per symbol
        Ts = n / (10**9)        # Ts for R_b = 1 Gb/s

        # Convert name to a unified bit-string
        binary = ''.join([char_to_binary(char) for char in name])

        # Padding if needed
        if len(binary) % n > 0:
            binary += '0' * (n - len(binary) % n)

        signal = np.array([])
        time = np.array([])
        N_symbols = len(binary) // n

        # Convert binary string to PPM signal
        for i in range(N_symbols):
            symbol_bits = binary[n*i:n*(i+1)]
            symbol = bit_to_symbol(symbol_bits, M)
            time_i, signal_i = ppm_modulation(symbol, Ts, M, Ts*i)
            signal = np.concatenate((signal, signal_i))
            time = np.concatenate((time, time_i))

        # Plotting
        plt.figure(figsize=(20, 5))
        plt.step(time, signal, where='post', color='b', linewidth=2)
        plt.title(f'Pulse Position Modulation (PPM) Signal (M = {M})')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.ylim([-0.2, 1.2])
        plt.grid(True)
        plt.show()


# Apply the function to plot PPM signals for the given name and M values
name = "Iasonas Karafotias"
M_array = [2, 4, 8, 16]
plot_ppm_signal(name, M_array)