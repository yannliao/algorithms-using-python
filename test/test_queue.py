# -*- coding: utf-8 -*-
"""
test code for linked list
"""
import context
import unittest
from src.listQueue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.testQueue = Queue()

    def tearDown(self):
        del self.testQueue

    def test_isEmpty(self):
        self.assertTrue(self.testQueue.isEmpty())
        self.assertEqual(len(self.testQueue), 0)

    def test_enqueue(self):
        self.testQueue.enqueue('item')
        self.assertFalse(self.testQueue.isEmpty())
        self.assertEqual(len(self.testQueue), 1)
        self.testQueue.enqueue('a')
        self.assertEqual(len(self.testQueue), 2)

    def test_dequeue(self):
        self.testQueue.enqueue('item1')
        self.testQueue.enqueue('item2')
        node1 = self.testQueue.dequeue()
        self.assertEqual(node1, 'item1')
        self.assertEqual(len(self.testQueue), 1)
        node2 = self.testQueue.dequeue()
        self.assertEqual(node2, 'item2')
        self.assertEqual(len(self.testQueue), 0)


if __name__ == '__main__':
    unittest.main()
