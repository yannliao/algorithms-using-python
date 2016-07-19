# -*- coding: utf-8 -*-
"""
  test code for the sort algorithms
"""

import context

import unittest
import src.sort as sort


class TestSortAlgorithms(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_bubble_sort(self):
        a = [8, 1, 4, 3, 4, 7, 6, 5]
        b = [1, 3, 4, 4, 5, 6, 7, 8]
        sort.bubbleSort(a)
        self.assertEqual(a, b)

    def test_selection_sort(self):
        a = [8, 1, 4, 3, 4, 7, 6, 5]
        b = [1, 3, 4, 4, 5, 6, 7, 8]
        sort.selectionSort(a)
        self.assertEqual(a, b)

    def test_insertion_sort(self):
        a = [8, 1, 4, 3, 4, 7, 6, 5]
        b = [1, 3, 4, 4, 5, 6, 7, 8]
        sort.insertionSort(a)
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()
