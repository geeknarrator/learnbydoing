class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        if s is None and len(dict) == 0:
            return s
        result = []
        length = len(s)
        bold = [False] * length

        for ind in range(0, length):
            max_found = -1
            for word in dict:
                if s.startswith(word, ind):
                    max_found = max(abs(len(word)+ind-1), max_found)
            if max_found >= 0:
                j = ind
                while j <= max_found:
                    bold[j] = True
                    j += 1
        i = 0
        while i < len(bold):
            if bold[i]:
                result.append("<b>")
                while i < len(bold) and bold[i]:
                    result.append(s[i])
                    i += 1
                result.append("</b>")
            else:
                result.append(s[i])
                i += 1

        return "".join(result)


print(Solution().addBoldTag("abcxyz123", ["abc", "123"]))
print(Solution().addBoldTag("aaabbcc", ["aaa", "aab", "bc"]))
