class linkList(object):
    """docstring for linkList"""
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        _listIterator(self._head)

    def search(self, target):
        curNode = self._head
        while curNode is not None and curNode.data != target:
            curNode = curNode.next
        return curNode is not None

    def insert(self, data):
        newNode = listNode(data)
        newNode.next = self._head
        self._head = newNode
        self._size += 1

    def delete(self, data):
        preNode = None
        curNode = self._head
        while curNode is not None and curNode.data != data:
            preNode = curNode
            curNode = curNode.next

        assert curNode is not None, "The item must be in the bag."
        self._size -= 1
        if curNode is self._head:
            self._head = curNode.next
        else:
            preNode.next = curNode.next
        return curNode.data


class _listIterator(self, head):
    def __init__(self, head):
        self.index = head

    def __iter__(self):
        retrun self

    def __next__(self):
        if self.index is None:
            raise StopIteration
        else:
            data = self.index.data
            self.index = self.index.next
            return data


class listNode:
    def __init__(self, data):
        self.data = data
        self.next = None
