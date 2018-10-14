def binary_search(items, item):
    start = 0
    end = len(items)-1

    while start <= end:
        mid = end - (end - start) // 2
        if items[mid] == item:
            return mid
        elif items[mid] > item:
            end = mid-1
        else:
            start = mid+1

    return -1

items= [1,2,3,4,5,6,7,8,9]
print(binary_search(items, 7))
print(binary_search(items, 10))