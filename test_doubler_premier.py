import unittest
from doubler_premier import doubler_premier, add, mul
from distance import distance


class TestDoublerPremier(unittest.TestCase):

    def test_doubler_premier_add(self):
        self.assertEqual(doubler_premier(add, 1, 4), 6)
        self.assertEqual(doubler_premier(add, 3, 4), 10)
        self.assertEqual(doubler_premier(add, 5, 4), 14)

    def test_doubler_premier_mul(self):
        self.assertEqual(doubler_premier(mul, 1, 4), 8)
        self.assertEqual(doubler_premier(mul, 3, 4), 24)
        self.assertEqual(doubler_premier(mul, 5, 4), 40)

    def test_doubler_premier_distance(self):
        self.assertEqual(doubler_premier(distance, 1.5, 4.0), 5.0)
        self.assertEqual(doubler_premier(distance, 2.0, 4.0, 4.0, 4.0), 8.0)


if __name__ == '__main__':
    unittest.main()
