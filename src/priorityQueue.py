# -*- coding: utf-8 -*-
"""
    implementation of Priority Queue using list
"""

from listQueue import Queue


class PriorityQueue:
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data) == 0

    def enqueue(self, item, priority):
        entry = _PriorityNode(item, priority)
        self.data.append(entry)

    def dequeue(self):
        assert not self.isEmpty(), "can not dequeue from an empty queue"
        highestPriority = self.data[0].priority
        highestindex = 0
        for i in range(len(self)):
            if self.data[i].priority > highestPriority:
                highestPriority = self.data[i].priority
                highestindex = i
        entry = self.data.pop(highestindex)
        return entry.item


class _PriorityNode:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
