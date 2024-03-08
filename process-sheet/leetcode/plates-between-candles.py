class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        plates_pos = []
        for p in range(len(s)):
            if s[p] == '|':
                plates_pos.append(p)
        ans = []
        for q in queries:
            end = bisect_right(plates_pos, q[1]) 
            start = bisect_left(plates_pos, q[0])
            if end > len(plates_pos) or start >= len(plates_pos) or q[1] == q[0]:
                ans.append(0)
                continue
            d = end - start -1
            res = plates_pos[end-1] - plates_pos[start] -d 
            if res > 0:
                ans.append(res)
            else:
                ans.append(0)
        return ans