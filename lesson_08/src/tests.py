import unittest
import random
from heap import heapsort

class TestHeapSort(unittest.TestCase):
    def setup(self):
        pass

    def test_sort_shuffle(self):
        lst = list(range(10))
        expected = list(range(10))
        actual = heapsort(lst)
        random.shuffle(lst)
        self.assertEqual(actual, expected)

    def test_sort_sorted(self):
        lst = list(range(10))
        expected = list(range(10))
        actual = heapsort(lst)
        random.shuffle(lst)
        self.assertEqual(actual, expected)


