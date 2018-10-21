class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_length = 0
        replace_index = -1
        current_length = 0
        replacements = k
        j = 1
        i = 0
        while i < len(s) and j < len(s):
            if s[i] == s[j]:
                current_length = j - i + 1
                j += 1
                print("curr", current_length)
            else:
                if replacements > 0:
                    replacements -= 1
                    if replace_index < 0:
                        replace_index = j
                    current_length = j - i + 1
                    print("curr if", current_length)
                    j += 1
                else:
                    max_length = max(max_length, current_length)
                    print("curr else", current_length)
                    current_length = 0
                    i = replace_index
                    replace_index = -1
                    j = i + 1
                    replacements = k
            max_length = max(max_length, current_length)
        return max_length


print(Solution().characterReplacement("AABABBA", 1))