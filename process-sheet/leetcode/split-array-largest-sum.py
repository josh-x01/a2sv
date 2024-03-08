class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        best = left

        while left <= right:
            mid = left + (right - left) // 2

            num_array = 1
            lsum = 0
            for i in range(len(nums)):
                lsum += nums[i]
                if lsum > mid:
                    lsum = nums[i]
                    num_array += 1
            
            if num_array > k:
                left = mid + 1
            else:
                best = mid 
                right = mid - 1
                
        return best
