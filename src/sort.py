# -*- coding: utf-8 -*-
"""
    A collection of sorting algorithms using python.
"""

from collections import deque


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
        insertion sort: iterate the list from the top to the end and move the
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


def mergeSort(sequence):
    """
    Sort the array in ascending order using merge sort
    """
    if len(sequence) <= 1:
        return sequence

    mid = len(sequence) // 2
    left = mergeSort(sequence[:mid])
    right = mergeSort(sequence[mid:])
    result = mergeSeq(left, right)
    return result


def mergeSeq(left, right):
    """
    Merge two sorted subsequences into one sorted list
    """
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


def partition(sequence, left, right):
    pivot = sequence[right]
    i = left - 1
    for j in range(left, right):
        if sequence[j] <= pivot:
            i += 1
            sequence[i], sequence[j] = sequence[j], sequence[i]

    sequence[i + 1], sequence[right] = sequence[right], sequence[i + 1]
    return i + 1


def quickSort(sequence, left, right):
    """
    sort the sequence using quick sort algorithm.
    """
    if left < right:
        pos = partition(sequence, left, right)
        quickSort(sequence, left, pos - 1)
        quickSort(sequence, pos + 1, right)


def countingSort(sequence, k):
    """
      Sorting array in O(n) time
    """
    count = [0 for _ in range(0, k)]
    bucket = [0] * len(sequence)
    # for i in range(0, k):
    #     C[i] = 0

    for ele in sequence:
        count[ele] += 1

    for i in range(1, k):
        count[i] += count[i - 1]

    for j in range(len(sequence) - 1, -1, -1):
        item = sequence[j]
        bucket[count[item] - 1] = sequence[j]
        count[item] -= 1
    return bucket


def radixSort(sequence, maxDigits):
    RADIX = 10
    placement = 1
    bucket = [deque() for _ in range(10)]

    for i in range(maxDigits):
        for ele in sequence:
            digit = (ele // placement) % RADIX
            bucket[digit].append(ele)
        j = 0
        for bin in bucket:
            for _ in range(len(bin)):
                sequence[j] = bin.popleft()
                j += 1

    placement *= RADIX


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
