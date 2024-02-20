class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        ans = 0
        gotOne = 0
        for k, v in count.items():
            if gotOne == 0 and (v == 1 or v % 2 != 0):
                gotOne = 1
            if v >= 2:
                if v % 2 == 0:
                    ans += v
                else:
                    ans += v-1
        return ans + gotOne