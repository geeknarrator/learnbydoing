## try and .. expect .. block
try:
    ## some code
except IOError:
    ## handler

try:
    f = open('somefile.txt', r)
    print(f.read())
    f.close()
except IOError:
    print('File not found')

# Throwing your own exception
raise IOError("File not found")
