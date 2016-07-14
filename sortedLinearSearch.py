def sortedLinearSearch(theList, item):
    length = len(theList)
    for i in range(length):
        if item == theList[i]:
            return True
        elif item < theList[i]:
            return False

    return False
