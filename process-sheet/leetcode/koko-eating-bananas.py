class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        _max = max(piles)
        def validHour(hour: int) -> int:
            total_hour = 0
            for p in piles:
                total_hour += ceil(p/hour)
            return total_hour
        
        left, right = 1, _max
        while left <= right:
            mid = left + (right - left) // 2
            res = validHour(mid)
            if res > h:
                left = mid + 1
            elif res <= h:
                right = mid - 1
        return left