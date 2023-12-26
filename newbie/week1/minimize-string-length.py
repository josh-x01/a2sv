class Solution:
    def minimizedStringLength(self, s: str) -> int:
        ss = {i for i in s}
        return len(ss)
        