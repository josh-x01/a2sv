class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        best = float('inf')
        while left <= right:
            mid = left + (right - left) // 2
            # print(mid)
            if nums[mid] >= nums[left]:
                best = min(best, nums[left])
                left = mid + 1
            else:
                best = min(best, nums[mid])
                right = mid - 1
        return best