from unittest import TestCase
from SumOfNumbers import get_sum

class Test(TestCase):
    def test_get_sum(self):
        self.assertEqual(get_sum(0, 1), 1)
        self.assertEqual(get_sum(0, -1), -1)

