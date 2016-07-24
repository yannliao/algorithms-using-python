# -*- coding: utf-8 -*-
"""
    test file for stack
"""

import context
import unittest
from src.listStack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        # print('In setUp()')
        self.testStack = Stack()

    def tearDown(self):
        # print('In tearDown()')
        del self.testStack

    def test_isEmpty(self):
        self.assertTrue(self.testStack.isEmpty(), 'isEmpty test fail')
        self.assertEqual(len(self.testStack), 0)

    def test_push(self):
        self.testStack.push('item')
        self.assertFalse(self.testStack.isEmpty(), 'push test fail')
        self.assertEqual(len(self.testStack), 1)

    def test_peek(self):
        self.testStack.push('item')
        item = self.testStack.peek()
        self.assertEqual(item, 'item')
        self.assertEqual(len(self.testStack), 1)
        self.assertEqual(self.testStack._top.next, None)

    def test_pop(self):
        self.testStack.push('item')
        item = self.testStack.pop()
        self.assertTrue(item, 'item')
        self.assertTrue(self.testStack.isEmpty())
        self.assertEqual(len(self.testStack), 0)

if __name__ == '__main__':
    unittest.main()
