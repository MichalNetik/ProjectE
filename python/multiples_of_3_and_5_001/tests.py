import unittest
from multiples_of_3_and_5_001.main import get_multiplies_sum
from utils.utils import timer

class GetMultiplesSumTests(unittest.TestCase):
    @timer
    def test_get_multiplies_sum_10(self):
        num = 10
        result = get_multiplies_sum(10)
        self.assertEqual(result, 23)

    @timer
    def test_get_multiplies_sum_100(self):
        num = 100
        result = get_multiplies_sum(num)
        self.assertEqual(result, 2318)

    @timer
    def test_get_multiplies_sum_1000(self):
        num = 1000
        result = get_multiplies_sum(num)
        self.assertEqual(result, 233168)
    
    @timer
    def test_get_multiplies_sum_100000(self):
        num = 100000
        result = get_multiplies_sum(num)
        self.assertEqual(result, 2333316668)

    @timer
    def test_get_multiplies_sum_10000000(self):
        num = 10000000
        result = get_multiplies_sum(num)
        self.assertEqual(result, 23333331666668)
