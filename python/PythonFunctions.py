def sum(start, end):
    result = 0
    for i in range(start, end):
        result+=i
    return result

print(sum(1,3))

# if return is used without any value None (special value in pyton) is returned

# if nothing is explicitly returned None is always returned
def none_return() :
    pass ## empty body

print(none_return()) # returns None

# Variable scope

x = 0 #global scope

def local_func():
    x = 1 #local scope
    print(x)


# assigning global scope
global globalx # assigns global scope to x

#Arguments with default
def default_arg(x=2, y=4):
    print("X : My default value is ",x)
    print("Y : My default value is ", y)

print(default_arg())

# Return multiple values from a function

def mult():
    return 1, 2

print(type(mult()))
