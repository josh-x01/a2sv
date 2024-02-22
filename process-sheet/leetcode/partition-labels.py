class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occ = {}

        for i in range(len(s)):
            last_occ[s[i]] = i

        anchor = j = 0
        ans = []
        for i in range(len(s)):
            j = max(j, last_occ[s[i]])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
        return ans
