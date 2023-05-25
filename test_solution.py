from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    """
    Стандартные случаи
    """
    def test_num_decoding_two_ways(self):
        sut = Solution()
        self.assertEqual(sut.numDecodings("12"), 2)

    def test_num_decoding_three_ways(self):
        sut = Solution()
        self.assertEqual(sut.numDecodings("226"), 3)

    def test_num_decoding_no_ways(self):
        sut = Solution()
        self.assertEqual(sut.numDecodings("06"), 0)

    """
    Граничащие значения
    """
    # 1 <= s.length <= 100
    def test_num_decoding_len_1(self):
        sut = Solution()
        self.assertEqual(sut.numDecodings("6"), 1)

    def test_num_decoding_len_2(self):
        sut = Solution()
        self.assertEqual(sut.numDecodings("66"), 1)

    def test_num_decoding_len_99(self):
        sut = Solution()
        string = "6"*99
        self.assertEqual(sut.numDecodings(string), 1)

    def test_num_decoding_len_100(self):
        sut = Solution()
        string = "6"*100
        self.assertEqual(sut.numDecodings(string), 1)

    def test_num_decoding_with_empty_string(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.numDecodings("")

    def test_num_decoding_with_len_101(self):
        sut = Solution()
        string = "6"*101
        with self.assertRaises(ValueError):
            sut.numDecodings(string)

    """
    Только цифры
    """
    def test_num_decoding_with_only_digits(self):
        sut = Solution()
        self.assertEqual(sut.numDecodings("6543210"), 1)

    def test_num_decoding_with_letters(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.numDecodings("abcde")

    def test_num_decoding_with_digits_and_letters(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.numDecodings("abcde12345")

    def test_num_decoding_with_ascii_symbols(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.numDecodings("@!$%@$^*.")
    """
    Нули
    """
    def test_num_decoding_with_zero(self):
        sut = Solution()
        self.assertEqual(sut.numDecodings("0"), 0)

    def test_num_decoding_with_zeros(self):
        sut = Solution()
        self.assertEqual(sut.numDecodings("00000000"), 0)
