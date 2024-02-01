class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=float("inf")
        l = 0
        r = 0
        _sum=0
        ch=0
        while r<len(nums):
            _sum+=nums[r]
            while _sum>=target:
                ans=min(ans,r-l+1)
                _sum-=nums[l]
                l+=1
                ch=1
            else:
                r+=1
        if ch==0:
            return 0
        return ans

        

                