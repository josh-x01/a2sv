class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        list_ =[x for x in nums if x!=0]
        count0 = nums.count(0)
        l1=[0]*count0
        list_.extend(l1)
        for i in range(len(nums)):
            nums[i]=list_[i]
        