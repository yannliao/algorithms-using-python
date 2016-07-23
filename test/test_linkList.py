# -*- coding: utf-8 -*-
"""
test code for linked list
"""

import context
import unittest
from src.linkList import LinkList


class TestLinkList(unittest.TestCase):
    def setUp(self):
        self.testList = LinkList()

    def tearDown(self):
        del self.testList

    def test_insert(self):
        self.testList.insert('a')
        self.assertTrue('a' in self.testList)

    def test_search(self):
        self.testList.insert('a')
        self.assertTrue(self.testList.search('a'))

    def test_delete(self):
        self.testList.insert('a')
        self.testList.insert('b')
        self.testList.delete('a')
        self.assertFalse(self.testList.search('a'))
        self.assertTrue(self.testList.search('b'))


if __name__ == '__main__':
    unittest.main()
