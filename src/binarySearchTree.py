# -*- coding: utf-8 -*-
"""
    implementation of Priority Queue using list
"""


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __contains__(self, key):
        return self._search(self._root, key) is not None

    def __setitem__(self, key, value):
        self.insertion(key, value)

    def __getitem__(self, key, value):
        return self._search(self.root, key)

    def _search(self, node, key):
        while node is not None and node.key != key:
            if node.key < key:
                node = node.left
            else:
                node = node.right
        return node

    def _tree_search(self, node, key):
        if node.key is None or node.key == key:
            return node
        elif node.key < key:
            self._tree_search(node.left, key)
        else:
            self._tree_search(node.right, key)

    def minimum(self, node):
        while node is not None:
            node = node.left
        return node

    def maxmum(self, node):
        while node is not None:
            node = node.right
        return node

    def successor(self, node):
        if node.right is not None:
            return self.minimum(node.right)
        flag = node.parent
        while flag is not None and node == flag.right:
            node = flag
            flag = flag.parent
        return flag

    def predecessor(self, node):
        if node.left is not None:
            return self.maxmum(node.left)
        flag = node.parent
        while flag is not None and node == flag.left:
            node = flag
            flag = flag.parent
        return flag

    def insertion(self, key, value):
        y = None
        x = self.root
        while x is not None and x.key != key:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right

        if x is not None:
            x.value = value
        elif key < y.key:
            y.left = Node(key, value, parent=y)
            self.size += 1
        else:
            y.right = Node(key, value, parent=y)
            self.size += 1

    def transplant(self, old, new):
        # only change the relationship with the parent node.
        if old.parent is None:
            self.root = new
        elif old == old.parent.left:
            old.parent.left = new
        else:
            old.parent.right = new
        if new is not None:
            new.parent = old.parent

    def deletion(self, key):
        node = self._search(self.root, key)
        assert node is not None, 'key is not in the tree'

        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        elif:
            successor = self.minimum(node.right)
            if node != successor.parent:
                self.transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor

            self.transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor


class Node:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
