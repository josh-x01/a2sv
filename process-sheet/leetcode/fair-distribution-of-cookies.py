class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_distribution = float('inf')
        distribution = [0] * k
        if len(cookies) == k:
            return max(cookies)

        def backtrack(i: int):
            nonlocal min_distribution, distribution
            if i >= len(cookies):
                min_distribution = min(min_distribution, max(distribution))
                return
            

            for j in range(k):
                distribution[j] += cookies[i]
                backtrack(i+1)
                distribution[j] -= cookies[i]
        backtrack(0)
        return min_distribution