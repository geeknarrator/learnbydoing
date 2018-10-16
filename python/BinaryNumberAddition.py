class BinaryNumber:
    def __init__(self, number):
        for c in number:
            if c!='0' or c!='1':
                raise BaseException("Invalid binary number")
        self.number = number

    def addBinary(self, A, B):
        small = B if len(A) > len(B) else A
        large = B if small is A else A
        small += "0" * (len(large) - len(small)) + small
        carry = 0
        result = ""
        s = len(small) - 1
        l = len(large) - 1
        while l >= 0 and s >= 0:
            binsum = int(small[s]) + int(large[l]) + int(carry)
            sum = binsum % 2
            result = str(sum) + result
            carry = binsum // 2
            s -= 1
            l -= 1

        if carry > 0:
            result = str(carry) + result

        return result


