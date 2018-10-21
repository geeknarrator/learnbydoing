def __init__(self, nestedList):
    """
    Initialize your data structure here.
    :type nestedList: List[NestedInteger]
    """
    self._nestedList = []
    self._flatten(nestedList)


def _flatten(self, nestedList):
    if len(nestedList) == 0:
        return
    i = 0
    while i < len(nestedList):
        if nestedList[i].isInteger():
            self._nestedList.append(nestedList[i].getInteger)
        else:
            self._flatten(nestedList[i].getList())
        i += 1


def next(self):
    """
    :rtype: int
    """
    return self._nestedList.pop()


def hasNext(self):
    """
    :rtype: bool
    """
    return len(self._nestedList) != 0
