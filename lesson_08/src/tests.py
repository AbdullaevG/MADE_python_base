import unittest
import random
from unittest.mock import patch
from io import StringIO

from heap import heapsort
import utils


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


class TesteMerge(unittest.TestCase):
    def setup():
        pass

    
    def test_merge2(self):
        """ merge the same elements of lists"""
        
        with patch('sys.stdout', new=StringIO()):
            lst1 = [1, 2, 4, 6, 7]
            lst2 = [2, 3, 4, 7, 8, 10]

            expected = [2, 4, 7]
            actual = utils.merge(lst1, lst2)
            self.assertEqual(actual, expected)

            lst1 = [1, 2, 2, 4, 6, 7]
            lst2 = [2, 2, 3, 4, 7, 8, 10]

            expected = [2, 4, 7]
            actual = utils.merge(lst1, lst2)
            self.assertEqual(actual, expected)

    def test_merge2_empty(self):
        """Merge two equal lists"""

        with patch('sys.stdout', new=StringIO()):
            lst1 = []
            lst2 = []

            expected = []
            actual = utils.merge(lst1, lst2)
            self.assertEqual(actual, expected)


    def test_mergek(self):
        """ merge the same elements of from k lists"""

        with patch('sys.stdout', new=StringIO()):
            lists = [[1, 2, 4, 6, 7], \
                     [2, 3, 4, 7, 8, 10]]

            expected = [2, 4, 7]
            actual = utils.merge_k(lists, len(lists))
            self.assertEqual(actual, expected)

