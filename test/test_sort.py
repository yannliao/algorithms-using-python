# -*- coding: utf-8 -*-
"""
  test code for the sort algorithms
"""

import context

import unittest
import random
import src.sort as sort


class TestSortAlgorithms(unittest.TestCase):
    def setUp(self):
        self.input = list(range(10))
        random.shuffle(self.input)
        self.correct = list(range(10))
        self.output = None

    def tearDown(self):
        del self.input
        del self.correct
        del self.output

    def test_bubble_sort(self):
        sort.bubbleSort(self.input)
        self.assertEqual(self.correct, self.input)

    def test_selection_sort(self):
        sort.selectionSort(self.input)
        self.assertEqual(self.correct, self.input)

    def test_insertion_sort(self):
        sort.insertionSort(self.input)
        self.assertEqual(self.correct, self.input)

    def test_merge_sort(self):
        self.output = sort.mergeSort(self.input)
        self.assertEqual(self.correct, self.output)

    def test_merge_sort(self):
        sort.quickSort(self.input, 0, len(self.input) - 1)
        self.assertEqual(self.correct, self.input)

    def test_counting_sort(self):
        self.output = sort.countingSort(self.input, 10)
        self.assertEqual(self.correct, self.output)

    def test_radix_sort(self):
        sort.radixSort(self.input, 2)
        self.assertEqual(self.correct, self.input)

    def test_heap_sort(self):
        sort.heapSort(self.input)
        self.assertEqual(self.correct, self.input)


if __name__ == '__main__':
    unittest.main()
