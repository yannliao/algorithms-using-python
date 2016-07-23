# -*- coding: utf-8 -*-
"""
    test file for stack
"""

import context
import unittest
from src.listStack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        print('In setUp()')
        self.testStack = Stack()

    def tearDown(self):
        print('In tearDown()')
        del self.testStack

    def test_isEmpty(self):
        self.assertTrue(self.testStack.isEmpty(), 'isEmpty test fail')

    def test_push(self):
        pass

if __name__ == '__main__':
    unittest.main()
