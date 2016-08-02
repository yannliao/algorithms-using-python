# -*- coding: utf-8 -*-
"""
    implementation of Map closed hashing
"""


class HashMap:
    UNUSED = None
    EMPTY = _MapEntry(None, None)

    def __init__(self):
        self._table = [None] * 7
        self._count = 0
        self._maxCount = len(self._table) - len(self._table) // 3

    def __len__(self):
        return self._count

    def __contain__(self, key):
        slot = self._findSlot(key, False)
        return slot is not None

    def _hash1(self, key):
        return abs(hash(key)) % len(self._table)

    def _hash2(self, key):
        return 1 + abs(hash(key)) % (len(self._table) - 2)

    def _findSlot(self, key, forInsert):
        slot = self._hash1(key)
        step = self._hash2(key)
        M = len(self._table)

        while self._table[slot] is not UNUSED:
            if forInsert and \
              (self._table[slot] is UNUSED or self._table[slot] is EMPTY):
                return slot
            elif not forInsert and \
              (self._table[slot] is not EMPTY and self._table[slot].key == key):
                return slot
            else:
                slot = (slot + step) % M

    def _rehash(self):
        origTable = self._table
        newSize = len(self._table) * 2
        self._table = [None] * newSize
        self._count = 0
        self._maxCount = newSize - newSize // 3
        for entry in origTable:
            if entry is not UNUSED and entry is not EMPTY:
                slot = self._findSlot(key, True)
                self._table[slot] = entry
                self._count += 1

    def add(self, key, value):
        pass

    def remove(self, key):
        pass

    def valueOf(self, key):
        slot = self._findSlot(key, False)
        assert slot is not None, "Invalid map key"
        return self._table[slot].value

    def __iter__(self):
        pass


class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
