def reverse(input):
    return input[::-1]

def reverse2(input):
    if len(input) is 0:
        return input
    return reverse2(input[1:]) + input[0]



#Given a string and an integer k, you need to reverse the
# first k characters for every 2k characters counting from
#  the start of the string. If there are less than k characters left,
# reverse all of them. If there are less than 2k but greater than or
# equal to k characters, then reverse the first k characters and left the other as original.
#Example:
#Input: s = "abcdefg", k = 2
#Output: "bacdfeg"

def reverseK(s, k):
    if len(s) < k:
        return reverse(s)
    elif len(s) < 2 * k & len(s) >= k:
        return reverse(s[0:k]) + s[k:]
    else:
        return reverse(s[0:k]) + s[k:2*k] + reverseK(s[2 * k:], k)


print(reverseK("abcdefg", 2))
print(reverseK("bawoopillu", 2))


#print(reverse2("A man, a plan, a canal: Panama"))