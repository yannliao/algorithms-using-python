# -*- coding: utf-8 -*-
"""
    implementation of max heap using list
"""


class Heap():
    """docstring for heap"""
    def __init__(self):
        self._heap_size = 0
        self._data = list()

    def __len__(self):
        return self._heap_size

    def _parent(self, index):
        return (index - 1) // 2

    def _left(self, index):
        return 2 * index + 1

    def _right(self, index):
        return 2 * index + 2

    def _shiftUp(self, index):
        parent = self._parent(index)
        while index > 0 and self._data[index] > self._data[parent]:
            self._data[index], self._data[parent] = \
              self._data[parent], self._data[index]
            index = parent
            parent = self._parent(index)

    def _shiftDown(self, index):
        l = self._left(index)
        r = self._right(index)
        if l <= self._heap_size and self._data[l] > self._data[index]:
            largest = l
        elif r <= self._heap_size and self._data[r] > self._data[index]:
            largest = r
        else:
            largest = index

        if largest != index:
            self._data[index], self._data[largest] = \
              self._data[largest], self._data[index]
            self._shiftDown(largest)

    def insert(self, key):
        self._data.append(key)
        self._heap_size += 1
        self._shiftUp(self._heap_size - 1)

    def extract(self):
        assert self._heap_size > 0, 'Heap underflow'
        max = self._data[0]
        self._data[0] = self._data.pop(self._heap_size - 1)
        self._heap_size -= 1
        self._shiftDown(0)
        return max
