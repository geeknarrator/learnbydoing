class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return True
        top = -1
        stack = []
        brackets = {'{':'}', '(':')', '[':']'}

        for c in s:
            if brackets.get(c) is not None:
                stack.append(c)
                top += 1
            else:
                top_c = stack.pop(top)
                top -= 1
                if brackets.get(top_c) != c:
                    return False
