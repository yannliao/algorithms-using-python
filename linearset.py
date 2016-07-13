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
        return item in self._data

    def __eq__(self, setB):
        # determins if two sets are equal.
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)

    def __iter__(self):
        # return an iterator for traversing the set.
        return Iterator(self._data)

    def add(self, item):
        # add a new element to the set.
        if item not in self._data:
            self._data.append(item)

    def remove(self, item):
        # remove an element in the set.
        assert element in self, "The element must be in the set."
        self._data.remove(item)

    def isSubsetOf(self, setB):
        # determin this set is a subset of setB.
        for element in self:
            if element not in setB:
                return False
        return True

    def union(self, setB):
        # create a new set from the union this set and setB.
        newSet = Set()
        newSet._data.extend(self._data)
        for element in setB:
            if element not in self:
                newSet._data.append(element)
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
