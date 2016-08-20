# -*- coding: utf-8 -*-
"""
    implementation of Priority Queue using list
"""

import binarySearchTree import BinarySearchTree

import binarySearchTree import Node as TreeNode


class AvlTree(BinarySearchTree):
    '''An extension t the BinarySearchTree data structure which
    strives to keep itself balanced '''

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
            self._updateBalance(y.left)
            self.size += 1
        else:
            y.right = Node(key, value, parent=y)
            self._updateBalance(y.right)
            self.size += 1

    def _rebalance(self, node):
        # node is the root of the unbalanced subtree.
        if node.balanceFactor < 0:
            if node.balanceFactor > 0:
                self._rotateRight(node.right)
                self._rotateLeft(node)
            else:
                self._rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.balanceFactor < 0:
                self._rotateLeft(node.left)
                self._rotateRight(node)
            else:
                self._rotateRight(node)
        return node

    def _updateBalance(self, node):
        while node is not None:
            if node.balanceFactor > 1 or node.balanceFactor < -1:
                self._rebalance(node)
                return
            if node.parent is not None:
                if node == node.parent.left:
                    node.parent.balanceFactor += 1
                elif node == node.parent.right:
                    node.parent.balanceFactor -= 1

                if node.parent.balanceFactor != 0:
                    node = node.parent
                else:
                    node = None

    def _rotateLeft(self, node):
        pass

    def _rotateRight(self, node):
        pass


class Node(TreeNode):
    def __init__(self, key, value, left=None, right=None, parent=None):
        TreeNode.__init__(key, value, left, right, parent)
        self.balanceFactor = 0
