class BinaryNumber:
    def __init__(self, number):
        for c in number:
            if c!='0' or c!='1':
                raise BaseException("Invalid binary number")
        self.number = number

    def add(self, binaryNumber):
        if binaryNumber is None:
            return self
        i1 = len(self.number)-1
        i2 = len(binaryNumber)-1
        carry=0
        while i1 >= 0 or i2 >= 0:


