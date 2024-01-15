class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        result = [0] * n
        result[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            result[i] = max(result[i+1], nums[i+1])
            
        min_ = nums[0]
        for i in range(1, n-1):
            if min_ < nums[i] < result[i]:
                return True
            min_ = min(min_, nums[i])
        return False