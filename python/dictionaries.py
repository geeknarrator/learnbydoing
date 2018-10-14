# Used to store key value pairs
friends = {
    "tom" : '190-1092-190910',
    "tommy" : '1902-19029-190290',
    "multi-tommy" : ['190902','1090192012']
}

print(friends)

# create an empty dictionary
empty_dict = {}

# get an item

# tomm = empty_dict['tomm']  # exception is thrown if no such key is found
print(friends['tom'])

friends['tom'] = '18982912' # modify tom's number
print(friends)

#friends['tom'].append('1i89892') throws an exception as toms value is string

friends['multi-tommy'].append("19209102") # since multi-tommy value is a list append works on that.
print(friends)

#Removing items from dict
del friends['tom']

print(friends)

#Looping elements in a dict
for key in friends:
    print(key, "number is", friends[key])

#length of the dictionary
print(len(friends))

#Remove everythin from the dictionary clear()
for i in friends.keys(): # returns all the keys
    print(i)

# remove item from dict pop()