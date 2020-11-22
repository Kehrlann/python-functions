import unittest
from numbers import numbers


class TestNumbers(unittest.TestCase):

    def test_numbers(self):
        self.assertEqual(numbers(), (0, 0, 0))
        self.assertEqual(numbers(6), (6, 6, 6))
        self.assertEqual(numbers(11, 9), (20, 9, 11))
        self.assertEqual(numbers(9, 6, 6, 13, 11), (45, 6, 13))
        self.assertEqual(numbers(9, 7, 15, 7), (38, 7, 15))
        self.assertEqual(numbers(11, 11, 12, 11, 5), (50, 5, 12))


if __name__ == '__main__':
    unittest.main()
