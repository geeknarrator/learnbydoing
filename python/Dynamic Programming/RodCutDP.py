import sys

def rodcut_recursive(pricearray, n):
    # pricearray denotes prices for length of rods.
    # n is the length of the rod
    # returns max revenue which can be achieved from the rod cut.
    if n == 0:
       return 0
    maxrevnue = -sys.maxsize - 1
    for i in range(1, n+1):
        subresult = pricearray[i]+rodcut_recursive(pricearray, n-i)
        maxrevnue = max(maxrevnue, subresult)
    return maxrevnue

def dp_rodcut(memory,pricearray, n):
    # pricearray denotes prices for length of rods.
    # n is the length of the rod
    # returns max revenue which can be achieved from the rod cut.
    memory.append(0)
    memory.append(pricearray[1])
    for i in range(2, n+1):
        maxrevenue = -sys.maxsize-1
        for j in range(1, i):
          maxrevenue = max(maxrevenue, pricearray[j]+memory[i-j])
        memory.append(max(pricearray[i], maxrevenue))
    return memory[n]



print(dp_rodcut([],[0,1,5,8,9,10,17,17,20,24,30],9))
print(rodcut_recursive([0,1,5,8,9,10,17,17,20,24,30],9))