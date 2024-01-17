class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        left = 0
        right = 0
        ans = 0

        operations = 0
        while right < n:
            if nums[right] != nums[right-1]:
                needed = nums[right] - nums[right-1]

                while ((needed * (right - left)) + operations) > k:
                    operations -= nums[right-1] - nums[left]
                    left += 1

                operations += (needed * ((right - left)))
            
            ans = max(ans, (right - left)+1)
            right += 1
        
        return ans