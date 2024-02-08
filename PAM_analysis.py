import numpy as np
import scipy as sp
from matplotlib import pyplot as plt


def Q_inv(y):
  """
  Calculate the inverse Q-Function using erfcinv for the tail probability of the standard normal distribution.

  The Q-function, Q(x) = 0.5 * erfc(x / sqrt(2)), relates to the complementary error function (erfc). Inverting
  this relationship, we use erfcinv to compute x = sqrt(2) * erfcinv(2y), mapping a Q-function value 'y' back
  to its 'x' value in the standard normal distribution's domain.

  :param y: Probability value for which the inverse Q-function is calculated.
  :return: The threshold value corresponding to the given probability in the context of a standard normal distribution.
  """
  return np.sqrt(2) * sp.special.erfcinv(2*y)


def get_snr(M, P_b):
  """
  Calculate the required Signal-to-Noise Ratio SNR for a given M-PAM system
  to achieve a specified bit error rate P_b based on the provided formula.

  This function implements the formula SNR = (M^2 - 1) / (6 * log2(M)) * Q_inv(...) ^ 2,
  where Q_inv is the inverse Q-function.

  :param M: The order of the PAM system.
  :param P_b: The desired probability of bit error.
  :return: The required SNR in dB to achieve the desired bit error probability.
  """
  SNR =  (M**2 - 1) / (6 * np.log2(M)) * Q_inv((M * np.log2(M) * P_b) / (2 * (M - 1)))**2
  SNR = 10*np.log10(SNR)   # Convert SNR from linear to decibels
  return SNR


def plot_snr_m(x, min_m=1, max_m=10):
    """
    Plot the required SNR in dB vs. the order of the PAM system M, for M values that are powers of 2.

    This function generates a plot to visualize how the required signal-to-noise ratio SNR in dB
    changes as a function of the PAM system's order M.

    :param x: The exponent used to calculate the bit error probability P_b = 10**(-2-x).
    :param min_m: Μinimum exponent of 2 for M values.
    :param max_m: Μaximum exponent of 2 for M values.
    :return:
    """
    P_b = 10 ** (-2 - x)
    M_values = [2 ** i for i in range(min_m, max_m + 1)]
    SNR_values = [get_snr(M, P_b) for M in M_values]

    plt.figure()
    plt.plot(M_values, SNR_values, 'o', linestyle='--')
    plt.xlabel('M')
    plt.ylabel('SNR (dB)')
    plt.title(f'SNR vs. M for P_b = $10^{{-2-{x}}}$')
    plt.grid(True)
    plt.show()


# Plot SNR-M for x=2 (AM=218142)
plot_snr_m(x=2)


# Example of get_snr application
M_example = 2
Pb_example = 1e-6
SNRb_dB_example = get_snr(M_example, Pb_example)
print(SNRb_dB_example)



