class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result=[]
        n=len(nums)
        
        for i in range(n):
            count=0
            for j in range(n):
                if(nums[i]>nums[j] and i!=j):
                    count+=1
            result.append(count)
        
        return result