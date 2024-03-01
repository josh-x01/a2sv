class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        candidates = list(range(1, min(10, n+1)))
        def backtrack(index, path, target):
            if len(path) == k and target == 0:
                ans.append(path[:])
                return
            if len(path) > k or target < 0:
                return
            
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                backtrack(i+1, path, target - candidates[i])
                path.pop()

        backtrack(0, [], n)
        return ans