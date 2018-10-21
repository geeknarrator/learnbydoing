class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = [] * (len(digits) + 1)
        carry = 1
        digit_sum = 0
        index = len(digits) - 1
        while index >= 0:
            digit_sum, carry = self.add_digit(digits, carry, index, result)
            index -= 1
        if carry > 0:
            result.append(carry)
        return result[::-1]

    def add_digit(self, digits, carry, index, result):
        digit_sum = digits[index] + carry
        carry = digit_sum // 10
        digit_sum = digit_sum % 10
        result.append(digit_sum)
        return digit_sum, carry

