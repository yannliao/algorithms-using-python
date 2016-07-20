# -*- coding: utf-8 -*-
"""
    A collection of sorting algorithms using python.
"""


def bubbleSort(sequence):
    """
        bubble sort re-arranges the values by iterating over the list multiple
        times, causing larger values to bubble to the  end of the list.
        time complexity of bubble sort is O(n^2).

        most inefficient sorting algorithms due to the
        total number of swaps required.
    """
    n = len(sequence)
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1):
        # Bubble the largest item to the end.
        for j in range(n - i - 1):
            if sequence[j] > sequence[j+1]:
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]


def bubbleSortUp(sequence):
    """
        bubble sort: bubble the smaller values to the top of the list.
    """
    n = len(sequence)
    for i in range(n - 1, -1, -1):
        for j in range(i, 0, -1):
            if sequence[j] < sequence[j - 1]:
                sequence[j - 1], sequence[j] = sequence[j], sequence[j - 1]


def selectionSort(sequence):
    """
        select sort: scan through the list and select the smallest item in the
        list then put it in a proper place.
        time complexity: O(n^2).

        The diference between the selection and bubble sorts is that
        the selection sort reduces the number of swaps
        required to sort the list to O(n)
    """
    n = len(sequence)
    # Assume the ith element is the smallest.
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            # print(j)
            if sequence[j] < sequence[smallest]:
                smallest = j
        sequence[i], sequence[smallest] = sequence[smallest], sequence[i]


def insertionSort(sequence):
    """
        insertion sort: iterte the list from the top to the end and move the
        key to the proper place step by step.
        time complexity: O(n^2)
    """
    n = len(sequence)
    for i in range(1, n):
        j = i - 1
        key = sequence[i]
        while j >= 0 and sequence[j] > key:
            sequence[j + 1] = sequence[j]
            j -= 1
        sequence[j + 1] = key


def mergeSortedLists(listA, listB):
    # merge two sorted lists into one.
    newList = list()
    a = 0
    b = 0
    while a < len(listA) and b < list(b):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a += 1
        else:
            newList.append(listB[b])
            b += 1

    while a < len(listA):
        newList.append(listA[a])
        a += 1
    while b < len(listB):
        newList.append(listB[b])
        b += 1

    return newList
