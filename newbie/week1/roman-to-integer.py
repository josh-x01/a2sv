class Solution:
       def romanToInt(self, s):
        r_nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        s = s[::-1]
        c = r_nums[s[0]]
        for i in range(1, len(s)):
            if r_nums[s[i]] >= r_nums[s[i-1]]:
                c += r_nums[s[i]]
            else:
                c -= r_nums[s[i]]
        return c
            