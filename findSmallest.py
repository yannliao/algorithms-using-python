def findSmallest(theList):
    small = theList[0]
    length = len(theList)
    for i in range(1, length):
        if theList[i] < small:
            small = theList[i]

    return small
