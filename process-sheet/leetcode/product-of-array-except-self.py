class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        suffix = [nums[-1]]
        length = len(nums)
        for i in range(1, length):
            prefix.append(prefix[-1] * nums[i])
            suffix.append(suffix[-1] * nums[-1 * i - 1])
        suffix.reverse()
        ans = []
        for i in range(length):
            if i == 0:
                ans.append(suffix[i+1])
            elif i == length - 1:
                ans.append(prefix[i-1])
            else:
                ans.append(prefix[i-1] * suffix[i+1])
        return ans
