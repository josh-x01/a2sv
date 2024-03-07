class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        _len = len(candidates)
        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if total > target or i >= _len:
                return
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i+1, cur, total)
        dfs(0, [], 0)
        return res