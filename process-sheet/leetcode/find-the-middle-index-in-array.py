class Solution:
    def findMiddleIndex(self, nums: [int]) -> int:
        prefixSum = [0]
        for i in range(len(nums)):
            prefixSum.append(prefixSum[i] + nums[i])
        for i in range(1, len(prefixSum)):
            print(prefixSum[i-1], prefixSum[-1], nums[i-1], prefixSum[i-1])
            if prefixSum[i-1] == prefixSum[-1] - nums[i-1] - prefixSum[i-1]:
                return i-1
        return -1