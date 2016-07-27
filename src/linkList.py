class LinkList():
    """docstring for linkList"""
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self, target):
        curNode = self._head
        while curNode is not None and curNode.data != target:
            curNode = curNode.next
        return curNode is not None

    def __iter__(self):
        return _listIterator(self._head)

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


class _listIterator:
    def __init__(self, head):
        self.index = head

    def __iter__(self):
        return self

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


"""
    doubly link list
"""


class CLinkList:
    """docstring for linkList"""
    def __init__(self):
        self._listRef = None
        self._size = 0

    def traverse(self):
        listRef = self._listRef
        curNode = listRef
        done = listRef is None
        while not done:
            curNode = curNode.next
            print(curNode.data)
            done = curNode is listRef

    def search(self, target):
        listRef = self._listRef
        curNode = listRef
        done = listRef is None
        while not done:
            curNode = curNode.next
            if curNode.data == target:
                return True
            else:
                done = curNode is listRef or curNode.data > target
        return False

    def insert(self, data):
        listRef = self._listRef
        newNode = CLinkNode(data)
        if listRef is None:
            listRef = newNode
            newNode.next = newNode
        elif data < listRef.next.data:
            newNode.next = listRef.next
            listRef.next = newNode
        elif data > listRef.data:
            newNode.next = listRef.next
            listRef.next = newNode
            listRef = newNode
        else:
            preNode = None
            curNode = listRef
            done = listRef is None
            while not done:
                predNode = curNode
                predNode = curNode.next
                done = curNode is listRef or curNode.data > data
            newNode.next = curNode
            preNode.next = newNode


class CLinkNode:
    def __init__(self, data):
        self.data = data
        self.next = None
