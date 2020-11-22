import unittest
from compare_args import compare_args
from utils import broken_fact, add, plus_broken
from math import factorial


class TestCompareArgs(unittest.TestCase):

    def test_compare_args_broken_fact(self):
        self.assertEqual(
            compare_args(broken_fact, factorial, [(0,), (1,), (5,)]),
            [False, True, True]
        )

    def test_compare_args_plus_broken(self):
        self.assertEqual(
            compare_args(plus_broken, add, [(2, 3), (0, 4), (4, 5)]),
            [True, False, True]
        )


if __name__ == '__main__':
    unittest.main()
