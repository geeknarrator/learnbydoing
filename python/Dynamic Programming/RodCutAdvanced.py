from itertools import permutations
import sys


def rodCut(A, B):
    if A == 0:
        return [0]
    perms = permutations(B)
    maxcost = -sys.maxsize-1
    result = []
    for perm in perms:
        totalcost = 0
        size = A
        for i, v in enumerate(perm):
            if i==0:
                totalcost+=size
            else:
                totalcost += size-v
                size=size-v
        if maxcost <= totalcost:
            maxcost = totalcost
            result.append(perm)

    return result

print(rodCut(6,[1,2,5]))

