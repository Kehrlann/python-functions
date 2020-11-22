import unittest
from distance import distance


class TestDistance(unittest.TestCase):

    def test_distance(self):
        self.assertEqual(distance(), 0.0)
        self.assertEqual(distance(1), 1.0)
        self.assertAlmostEqual(distance(1, 1), 1.41421, 5)
        self.assertAlmostEqual(distance(1, 1, 1), 1.73205, 5)
        self.assertEqual(distance(1, 1, 1, 1), 2.0)
        self.assertAlmostEqual(
            distance(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 16.88194, 5)


if __name__ == '__main__':
    unittest.main()
