class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        prefixSum = [0]
        for i in range(len(nums)):
            prefixSum.append(prefixSum[i] + nums[i])
        l = 0
        score = 0
        checked = {}
        _len = len(nums)
        for r in range(_len):
            if nums[r] not in checked or checked[nums[r]] < l:
                checked[nums[r]] = r
                if r == _len - 1:
                   score = max(score, prefixSum[r+1] - prefixSum[l]) 
                continue
            
            score = max(score, prefixSum[r] - prefixSum[l])
            # print(l, r, checked, nums[r])
            
            l = checked[nums[r]] + 1
            checked[nums[r]] = r
        return score

            

        