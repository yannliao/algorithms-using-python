# -*- coding: utf-8 -*-
"""
    Kinds of search algorithms
"""


def sortedLinearSearch(theList, item):
    """
        linear search: find the item in the list by iterate the entire list.
        time complexity of linear search is O(n).
    """
    length = len(theList)
    for i in range(length):
        if item == theList[i]:
            return True
        elif item < theList[i]:
            return False

    return False


def findSmallest(theList):
    small = theList[0]
    length = len(theList)
    for i in range(1, length):
        if theList[i] < small:
            small = theList[i]

    return small


def binarySearch(theList, item):
    """
        binary search use the divide and conquer stratigy, which first divide a
        larger problem into similar small problems
        then conquer the smaller part.
        time complexity of binary search is O(log n)

    """
    low = 0
    high = len(theList) - 1
    while low <= high:
        mid = (high + low) // 2
        if theList[mid] == item:
            return True
        elif item < theList[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False
