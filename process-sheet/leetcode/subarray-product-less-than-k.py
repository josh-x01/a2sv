class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        product = 1
        subarrays = 0
        while j < len(nums):
            if product * nums[j] < k:
                product *= nums[j]
                j += 1
            elif i < j:
                subarrays += j - i
                product //= nums[i]
                i += 1
            else:
                i += 1
                j += 1
        if i < j:
            n = j - i
            subarrays += n * (n + 1) // 2
        return subarrays