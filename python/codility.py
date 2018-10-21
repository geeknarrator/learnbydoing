# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import heapq

def solution(A, X, Y, Z):
    # write your code in Python 3.6
    wait_time=0
    heap = []
    heapq.heappush(heap, (0,X))
    heapq.heappush(heap, (0,Y))
    heapq.heappush(heap, (0,Z))

    tmp = []
    i = 0
    while i < len(A):
        if not heap:
            return -1
        wait, fuel = heapq.heappop(heap)
        if A[i] <= fuel:
            wait_time = max(wait, wait_time)
            new_fuel = fuel - A[i]
            new_wait = wait + A[i]
            heapq.heappush(heap, (new_wait, new_fuel))
            for item in tmp:
                heapq.heappush(heap, item)
            tmp = []
            i += 1
        else:
            tmp.append((wait, fuel))

    return wait_time


print(solution([2,8,4,3,2],0,0,0))





            