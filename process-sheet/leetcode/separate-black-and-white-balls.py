class Solution:
    def minimumSteps(self, s: str) -> int:
        left = 0
        _len = len(s)
        while s[left] != '1':
            left += 1
            if left > _len - 1:
                return 0
        ans = 0
        for right in range(left+1, _len):
            if s[right] == '0':
                ans += right - left
                left += 1
        return ans