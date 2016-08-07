# -*- coding: utf-8 -*-
"""
test code for linked list
"""
import context
import unittest
from src.linearheap import Heap


class TestHeap(unittest.TestCase):
    def setUp(self):
        self.testHeap = Heap()
        self.testHeap._data = [100, 84, 71, 60, 23, 12, 29, 1, 37, 4]
        self.testHeap._heap_size = 10

    def tearDown(self):
        del self.testHeap

    def test_insert(self):
        correct = [100, 90, 71, 60, 84, 12, 29, 1, 37, 4, 23]
        self.testHeap.insert(90)
        self.assertEqual(self.testHeap._data, correct)
        self.assertEqual(len(self.testHeap), 11)

    def test_extract(self):
        correct = [84, 60, 71, 37, 23, 12, 29, 1, 4]
        output = self.testHeap.extract()
        self.assertEqual(self.testHeap._data, correct)
        self.assertEqual(len(self.testHeap), 9)
        self.assertEqual(output, 100)

if __name__ == '__main__':
    unittest.main()
