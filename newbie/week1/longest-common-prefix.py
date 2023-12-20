class Solution:
    def longestCommonPrefix(self, strs):
        if (len(strs) == 1):
            return strs[0]
        s = ""
        for i in strs[0]:
            s += i
            for j in range(len(strs)):
                if (j == 0):
                    continue
                if (s == strs[j][:len(s)]):
                    continue
                return s[:-1]
        return s