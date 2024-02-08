import unittest
from PPM_generator import ppm_modulation, char_to_binary, bit_to_symbol


class TestPPMMethods(unittest.TestCase):

    def test_char_to_binary(self):
        """
        Test the ASCII to binary conversion
        """
        result = char_to_binary('A')  # Assuming 'A' should convert to '01000001'
        self.assertEqual(result, '01000001', "The binary conversion of 'A' is incorrect")


    def test_bit_to_symbol(self):
        """
        Test the Gray code conversion for M=4
        """
        result = bit_to_symbol('01', 4)
        self.assertEqual(result, 1, "Gray code conversion for '01' is incorrect")


    def test_ppm_modulation(self):
        """
        Test PPM modulation for a known symbol and M value
        """
        Ts = 1e-9  # Symbol duration
        M = 2
        symbol = 0  # Test symbol
        t_start = 0  # Starting time
        time, signal = ppm_modulation(symbol, Ts, M, t_start)
        # Check if signal is high only within the expected time frame
        expected_high_start = t_start + (symbol * Ts / M)
        expected_high_end = t_start + ((symbol + 1) * Ts / M)
        for t, s in zip(time, signal):
            if expected_high_start <= t < expected_high_end:
                self.assertEqual(s, 1, "Signal should be high within the symbol duration")
            else:
                self.assertEqual(s, 0, "Signal should be low outside the symbol duration")


if __name__ == '__main__':
    unittest.main()
