input = "[]{}[}{}"

# Creating list in python
l = [1, 2, 3, "4"]

for i in l:
    print(i)

#Other ways
newlist = list()
newList = list([1,2,3,4])
newListOfchars = list("python")

for c in newListOfchars:
    print(c)

#accesing items in a list
print("I am the first character : ",newListOfchars[0])

#length of list
print(len(newListOfchars))
print(max(newList))
print(min(newList)) # min from the list
print(sum(newList)) ## sum of all items in the list


#If element is in the list or not
if 1 in newList:
    print("new list contains 1")

#Concatenates two sequences
print(newList+newListOfchars)

for loop in newListOfchars+newList:
    print(loop)

#List slicing
print(newList[1:3])

# + and * operator on list
print(newList*3)

print((newList+newListOfchars)*3)

#Count number of times and item exists in the list
print((newList).count(1))
newList.insert(1, 2) #inserts 2 at index 1
print(newList.index(2)) #finds first index of 2 in newlist
print(newList)

print(newList.reverse()) #reverse a list
newList.pop() # removes last element
x = newList.pop(1) # removes element at index 1
print(x)

print(newList)

#Comprehension of lists
list = [x for x in range(0,10)]
evenlist = [x for x in range(0,10) if x%2==0]
print(evenlist)





