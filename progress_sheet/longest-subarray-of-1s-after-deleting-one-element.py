class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nums = "".join([str(i) for i in nums]).split('0')
        print(nums)
        max_ = 0
        l = len(nums)
        if l == 1:
            return len(nums[0]) - 1
        
        for i in range(1, l):
            max_ = max(max_, len(nums[i]) + len(nums[i-1]))



        
        return max_
