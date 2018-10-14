def fibonacci(num):
    if num is 0:
        return 1
    elif num is 1:
        return 1
    fib = [1, 1]
    for i in range(2, num):
        fib.append(fib[i-1]+fib[i-2])
    return fib[num-1]


print(fibonacci(10))