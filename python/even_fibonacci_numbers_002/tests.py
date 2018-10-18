import unittest
from even_fibonacci_numbers_002.main import get_fibonacci_sum

class FibonacciTest(unittest.TestCase):
    def test_lesser_than_10(self):
        result = get_fibonacci_sum(10)
        self.assertEqual(result, 10)

    def test_lesser_than_100(self):
        result = get_fibonacci_sum(100)
        self.assertEqual(result, 44)
      