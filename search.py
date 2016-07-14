def sortedLinearSearch(theList, item):
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
