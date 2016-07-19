# -*- coding: utf-8 -*-
"""
    implementation of map using list
"""


class Map:
    """docstring for Map"""
    def __init__(self):
        self._entryList = list()

    def __len__(self):
        return len(self._entryList)

    def __contains__(self, key):
        index = self._findPosition(key)
        return index is not None

    def __iter__(self):
        return self

    # finde the position of the key , if key is not found return None else
    # return the position
    def _findPosition(self, key):
        for i in range(len(self)):
            if self._entryList[i].key == key:
                return i
        return None

    # Add a key/value pair to the map if the key does not exist. Otherwise,
    # replace the old value with the new one.
    def add(key, value):
        index = self._findPosition(key)
        if index is None:
            entry = _MapEntry(key, value)
            self._entryList.append(entry)
            return True
        else:
            self._entryList[index].value = value
            return False

    # Removes the entry associated with the key.
    def remove(self, key):
        index = self._findPosition(key)
        assert index is not None, 'Invalid map key.'
        self._entryList.pop(index)

    # Returns the value associated with the key.
    def valueOf(self, key):
        index = self._findPosition(key)
        assert index is not None, 'Invalid map Key.'
        return self._entryList[index].value


class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
