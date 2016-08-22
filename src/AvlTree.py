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
            self._insertionUpdateBalance(y.left)
            self.size += 1
        else:
            y.right = Node(key, value, parent=y)
            self._insertionUpdateBalance(y.right)
            self.size += 1

    def _deleteUpdateBalance(self, node):
        while node is not None:
            # if node.balanceFactor > 1 or node.balanceFactor < -1:
            #     self._rebalance(node)
            #     return
            if node.parent is not None:
                if node == node.parent.left:
                    node.parent.balanceFactor -= 1
                elif node == node.parent.right:
                    node.parent.balanceFactor += 1

                if node.parent.balanceFactor == 0:
                    node = node.parent
                else:
                    node = None

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

    def _insertionUpdateBalance(self, node):
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
        newRoot = node.right
        node.right = newRoot.left
        if node.right is not None:
            node.right.parent = node
        newRoot.parent = node.parent

        if node is self.root:
            self.root = newRoot
        else:
            if node == node.parent.left:
                node.parent.left = newRoot
            else:
                node.parent.right = newRoot
        newRoot.left = node
        node.parent = newRoot

        node.balanceFactor = node.balanceFactor + 1 - \
            min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + \
            max(node.balanceFactor, 0)
        return newRoot

    def _rotateRight(self, node):
        newRoot = node.left
        node.left = newRoot.right
        if node.left is not None:
            node.left.parent = node
        newRoot.parent = node.parent

        if node is self.root:
            self.root = newRoot
        else:
            if node == node.parent.left:
                node.parent.left = newRoot
            else:
                node.parent.right = newRoot

        newRoot.right = node
        node.parent = newRoot
        node.balanceFactor = node.balanceFactor - 1 - \
            max(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + \
            min(node.balanceFactor, 0)


class Node(TreeNode):
    def __init__(self, key, value, left=None, right=None, parent=None):
        TreeNode.__init__(key, value, left, right, parent)
        self.balanceFactor = 0
