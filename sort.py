# A collection of sorting algorithms using python.


def bubbleSort(sequence):
    n = len(sequence)
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1):
        # Bubble the largest item to the end.
        for j in range(n - i - 1):
            if sequence[j] > sequence[j+1]:
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]


def selectionSort(sequence):
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
    n = len(sequence)
    for i in range(1, n):
        j = i - 1
        key = sequence[i]
        while j >= 0 and sequence[j] > key:
            sequence[j + 1] = sequence[j]
            j -= 1
        sequence[j + 1] = key
