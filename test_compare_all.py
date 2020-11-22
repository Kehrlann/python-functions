import unittest
from compare_all import compare_all
from utils import fact, broken_fact
from math import factorial


class TestCompareAll(unittest.TestCase):

    def test_compare_all_fact(self):
        self.assertEqual(
            compare_all(fact, factorial, [0, 1, 5]),
            [True, True, True]
        )

    def test_compare_all_broken_fact(self):
        self.assertEqual(
            compare_all(broken_fact, factorial, [0, 1, 5]),
            [False, True, True]
        )


if __name__ == '__main__':
    unittest.main()
