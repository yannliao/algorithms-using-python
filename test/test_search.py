# -*- coding: utf-8 -*-
"""
  test code for the search algorithms
"""

import context

import unittest
import src.search as search


class TestSearchAlgorithms(unittest.TestCase):
    def setUp(self):
        self.testList = [0, 1, 2, 3, 4, 5, 6, 7]

    def tearDown(self):
        del self.testList

    def test_findSmallest(self):
        self.assertEqual(search.findSmallest(self.testList), 0)

    def test_sortedLinearSearch(self):
        self.assertTrue(search.sortedLinearSearch(self.testList, 4))
        self.assertFalse(search.sortedLinearSearch(self.testList, 8))

    def test_binarySearch(self):
        self.assertTrue(search.sortedLinearSearch(self.testList, 4))
        self.assertFalse(search.sortedLinearSearch(self.testList, 8))

if __name__ == '__main__':
    unittest.main()
