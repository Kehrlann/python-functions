import unittest
from doubler_premier_kwds import doubler_premier_kwds, add3, mul3
from distance import distance


class TestDoublerPremier(unittest.TestCase):

    def test_doubler_premier_kwds_add(self):
        self.assertEqual(doubler_premier_kwds(add3, 1, 2, 3), 7)
        self.assertEqual(doubler_premier_kwds(add3, 1, 2, z=3), 7)
        self.assertEqual(doubler_premier_kwds(add3, 1, y=2, z=3), 7)

    def test_doubler_premier_kwds_mul(self):
        self.assertEqual(doubler_premier_kwds(mul3, 1, 2, 3), 12)
        self.assertEqual(doubler_premier_kwds(mul3, 1, 2, z=3), 12)
        self.assertEqual(doubler_premier_kwds(mul3, 1, z=2, y=3), 12)

    def test_doubler_premier_kwds_distance(self):
        self.assertEqual(doubler_premier_kwds(distance, 1.5, 4.0), 5.0)
        self.assertEqual(doubler_premier_kwds(
            distance, 2.0, 4.0, 4.0, 4.0), 8.0)


if __name__ == '__main__':
    unittest.main()
