class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        counter = Counter(nums)
        minimum = nums[0]
        index = len(nums)-1
        while index>-1 and nums[index]==nums[len(nums)-1]:
            index-=1
        if index==-1:
            return 0
        total = value = counter[nums[index+1]]
        while nums[index]>minimum:
            if nums[index]!=nums[index+1]:
                total+=value+counter[nums[index]]
                value+=counter[nums[index]]
            index-=1
        return total