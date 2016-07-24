# -*- coding: utf-8 -*-
"""
    implementation of Queue using linked list
"""


class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    def __len__(self):
        return self._count

    def isEmpty(self):
        return self._head is None

    def enqueue(self, item):
        node = _QueueNode(item)
        if self._head is None:
            self._head = node
        else:
            self._tail.next = node
        self._tail = node
        self._count += 1

    def dequeue(self):
        assert not self.isEmpty(), "can not dequeu from an empty queue"
        node = self._head
        self._head = self._head.next
        self._count -= 1
        if self._head is self._tail:
            self._tail = None
        return node.item


class _QueueNode:
    def __init__(self, item):
        self.item = item
        self.next = None
