class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        sl = [''] * len(s)
        for i in range(len(s)):
            sl[indices[i]] = s[i]
        return "".join(sl)