# -*- coding: utf-8 -*-
"""
test code for linked list
"""

import context
import unittest
from src.linkList import LinkList


class TestLinkList(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_insert(self):
        testList = LinkList()
        testList.insert('a')
        # for element in testList:
        #     print(element)
        # self.assertTrue('a' in LinkList)

    def test_search(self):
        testList = LinkList()
        testList.insert('a')
        self.assertTrue(testList.search('a'))

    def test_delete(self):
        testList = LinkList()
        testList.insert('a')
        testList.insert('b')
        testList.delete('a')
        self.assertFalse(testList.search('a'))
        self.assertTrue(testList.search('b'))


if __name__ == '__main__':
    unittest.main()
