class Solution:
    def countPairs(self, nums, k):
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if ((i*j) % k == 0):
                    if (nums[i] == nums[j]):
                        count += 1
        return count
