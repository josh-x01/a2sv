class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = maxSum = sum(nums[0:k])

        for i in range(len(nums)):
            if k+i == len(nums):
                break
            print(currSum)
            currSum += nums[k+i] - nums[i]
            maxSum = max(maxSum, currSum)
    
        return maxSum/k