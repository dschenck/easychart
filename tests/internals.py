import unittest
import easychart.internals as internals


class Test(unittest.TestCase):
    def test_flatten(self):
        self.assertEqual(internals.flatten(1), [1])
        self.assertEqual(internals.flatten(1, 2, 3), [1, 2, 3])
        self.assertEqual(internals.flatten(1, [2, 3]), [1, 2, 3])
