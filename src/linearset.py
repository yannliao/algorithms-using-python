# -*- coding: utf-8 -*-
"""
    implementation of Set using list
"""


class Set:
    """Implementation of a set ADT using Python list"""
    def __init__(self):
        # creat a empty set
        self._data = list()

    def __len__(self):
        # return the munbers of item in the set.
        return len(self._data)

    def __contains__(self, item):
        # determin weather an item is in the set. if exits return true.
        # return item in self._data
        index = self._findPosition(item)
        return index < len(self) and self._data[index] == item

    def __eq__(self, setB):
        # determins if two sets are equal.
        # if len(self) != len(setB):
        #     return False
        # else:
        #     return self.isSubsetOf(setB)
        if len(self) != len(setB):
            return False
        else:
            for i in range(len(self)):
                if self._data[i] != setB[i]:
                    return False

            return True

    def __iter__(self):
        # return an iterator for traversing the set.
        return Iterator(self._data)

    def _findPosition(self, item):
        high = len(self) - 1
        low = 0
        while low <= high:
            mid = (high + low) // 2
            if item == self._data[mid]:
                return mid
            elif item < self._data[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return low

    def add(self, item):
        # add a new element to the set.
        # if item not in self._data:
        #     self._data.append(item)
        if item not in self:
            index = self._findPosition(item)
            self._data.insert(index, item)

    def remove(self, item):
        # remove an element in the set.
        assert element in self, "The element must be in the set."
        # self._data.remove(item)
        index = self._findPosition(item)
        self._data.pop(index)

    def isSubsetOf(self, setB):
        # determin this set is a subset of setB.
        for element in self:
            if element not in setB:
                return False

        return True

    def union(self, setB):
        # create a new set from the union this set and setB.
        # newSet = Set()
        # newSet._data.extend(self._data)
        # for element in setB:
        #     if element not in self:
        #         newSet._data.append(element)
        # return newSet
        newSet = Set()
        i = 0
        j = 0
        while i < len(self) and j < len(setB):
            if self._data[i] < setB._data[j]:
                newSet._date.append(self._data[i])
                i += 1
            elif self._data[i] > setB._data[j]:
                newSet._date.append(setB._data[j])
                j += 1
            else:
                # Only one of the two duplicates are appended.
                newSet._date.append(setB._data[j])
                i += 1
                j += 1

        while i < len(self._data[i]):
            newSet._data.append(self._data[i])

        while j < len(setB):
            newSet._data.append(setB._data[j])

        return newSet

    def interset(self, setB):
        # create a new set from the intersect of this set and setB.
        pass

    def difference(self, setB):
        # create a new set from the difference of two sets.
        pass


class Iterator:
    def __init__(self, data):
        self._data = data
        self._index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index == 0:
            raise StopIteration
        self._index -= 1
        return self._data[self._index]
