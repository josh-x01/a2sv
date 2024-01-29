class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        result=0
        zero=0
        left=0
        for r in range(len(nums)):
            if nums[r]==0:
                zero+=1
            while left<len(nums) and zero>k:
                if nums[left]==0:
                    zero-=1
                left+=1
            result=max(result,r-left+1)
        return result
            