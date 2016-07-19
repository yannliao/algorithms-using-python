# -*- coding: utf-8 -*-
"""
  test code for the search algorithms
"""

import context

import unittest
import src.search as search


class TestSearchAlgorithms(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_findSmallest(self):
        a = [1, 3, 9, 4, 2, 0]
        self.assertEqual(search.findSmallest(a), 0)

    def test_sortedLinearSearch(self):
        a = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertTrue(search.sortedLinearSearch(a, 4))
        self.assertFalse(search.sortedLinearSearch(a, 8))

    def test_binarySearch(self):
        a = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertTrue(search.sortedLinearSearch(a, 4))
        self.assertFalse(search.sortedLinearSearch(a, 8))

if __name__ == '__main__':
    unittest.main()
