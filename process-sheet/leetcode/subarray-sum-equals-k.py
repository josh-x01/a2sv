class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        _dict = defaultdict(int)
        prefixSum = [0]
        for i in range(len(nums)):
            prefixSum.append(prefixSum[i] + nums[i])
        for i in range(len(prefixSum)):
            curValue = prefixSum[i] - k
            ans += _dict[curValue]
            _dict[prefixSum[i]] += 1
        return ans
        