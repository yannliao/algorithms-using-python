# -*- coding: utf-8 -*-
"""
test code for linked list
"""
import context
import unittest
from src.priorityQueue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.testQueue = PriorityQueue()

    def tearDown(self):
        del self.testQueue

    def test_isEmpty(self):
        self.assertTrue(self.testQueue.isEmpty())
        self.assertEqual(len(self.testQueue), 0)

    def test_enqueue(self):
        self.testQueue.enqueue('purple', 5)
        self.assertFalse(self.testQueue.isEmpty())
        self.assertEqual(len(self.testQueue), 1)
        self.testQueue.enqueue('black', 1)
        self.assertEqual(len(self.testQueue), 2)

    def test_dequeue(self):
        self.testQueue.enqueue('purple', 5)
        self.testQueue.enqueue('black', 1)
        self.testQueue.enqueue("white", 0)
        self.testQueue.enqueue("green", 1)
        self.testQueue.enqueue("yellow", 5)
        node1 = self.testQueue.dequeue()
        self.assertEqual(node1, 'purple')
        self.assertEqual(len(self.testQueue), 4)
        node2 = self.testQueue.dequeue()
        self.assertEqual(node2, 'yellow')
        self.assertEqual(len(self.testQueue), 3)
        node3 = self.testQueue.dequeue()
        self.assertEqual(node3, 'black')
        self.assertEqual(len(self.testQueue), 2)


if __name__ == '__main__':
    unittest.main()
