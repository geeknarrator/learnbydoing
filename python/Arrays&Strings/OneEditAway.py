class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_s = {}
        char_t = {}
        for i in range(len(s)):
            if char_s.get(s[i]) is None:
                char_s[s[i]] = 1
            else:
                count = char_s.get(s[i])
                char_s[s[i]] = count + 1

        for i in range(len(t)):
            if char_t.get(t[i]) is None:
                char_t[t[i]] = 1
            else:
                count = char_t.get(t[i])
                char_t[t[i]] = count + 1

        print(char_s)
        print(char_t)
        for k, v in char_s.items():
            if char_t.get(k) is not None:
                count = char_t.get(k)
                if count == 1:
                    del char_t[k]
                else:
                    char_t[k] = count - 1
                if v == 1:
                    del char_s[k]
                else:
                    char_s[k] = v - 1


Solution().isOneEditDistance("abcc","acc")