class Solution:
    def twonumsum(self, num1, num2):
        small = num2 if len(num1) > len(num2) else num1
        large = num1 if len(num1) > len(num2) else num2
        small = "0" * (len(large) - len(small)) + small
        carry = 0
        result = ""
        i = len(large) - 1
        while i >= 0:
            sum = int(small[i]) + int(large[i]) + carry
            carry = sum // 10
            sum = sum % 10
            result = str(sum) + result
            i -= 1

        if carry > 0:
            result = str(carry) + result

        return result

    def listsum(self, mults):
        if len(mults) == 0:
            return 0
        if len(mults) == 1:
            return mults[0]
        final_sum = mults[0]
        i = 1
        while i < len(mults):
            final_sum = self.twonumsum(final_sum, mults[i])
            i += 1
        return final_sum

    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        if A == "0" or B == "0":
            return "0"
        # to store each multiplication
        mults = []
        count = 0
        ia=len(A)-1
        ib=len(B)-1
        for ca in A[::-1]:
            mult = ""
            carry = 0
            multiplier = "0"
            for cb in B[::-1]:
                num = int(cb) * int(ca) + carry
                carry = num // 10
                mult = str(num % 10) + mult
            mult = mult + (multiplier * count)
            count+=1

            if carry > 0:
                mult = str(carry) + mult
            mults.append(mult)

        return self.listsum(mults)



#print(Solution().multiply("5131848155574784703269632922904933776792735241197982102373370","56675688419586288442134264892419611145485574406534291250836"))
print(Solution().multiply("010","1"))
#print(Solution().listsum(["900","800","100","99999"]))




