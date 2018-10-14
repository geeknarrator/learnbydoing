print("hello")

x = 100
pi = 3.14
empname = "python is great"

a = b = c = 100

# I am a comment
print("Hello world")
x = 1
y = 2
y, x = x, y
print(x)
print(y)

#Number data type
i = 100
f = 12.5
print(type(f))

#Python operators
print(3//2)
print(3**2)

#Strings in python
name = "tom"
emptyname = str()
fillname = str("name")
fillname2="name"
print(fillname[0])
s = "tom " + "jerry "

#repeats the string using multiplication operator
s = s*3
print(s)

#String slicing in python
name="helloname"
print(name[:])

#ascii code of the char
print(ord('a'))

#char for a given ascii
print(chr(900))

print(len("mylength"))

#max(string) given char with max ascii code and min(string) returns min char
print(max("mylength"),min("mylength"))


## in and not in operator
s1 = "Welcome"
if "come" in s1: #"come" not in s1
    print("I am a substring")
else:
    print("I am not a substring")


s2 = "you are not welcome"
print(s1 > s2) ## compares two string in lexicographical order based on ascii value


#Iterating string using loop
for i in s1:
    print(i, end ="\n")

# checking if a string is alphnumeric
if s1.isalnum():
    print("I am alphanumeric")

# Similarly isalpha() isdigit() isidentifier() islower() isuppper() isspace()

# Check is a string endswith "thon"

print("python".endswith("thon"))
print("python".startswith("py"))

print("python".replace("tho", "the"))



