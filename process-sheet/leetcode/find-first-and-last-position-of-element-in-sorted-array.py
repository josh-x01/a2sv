class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        _len = len(nums)
        left, right = 0, len(nums) - 1
        start, end = -1, -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = right = mid
                while left >= 0 and nums[left] == target:
                    left -= 1
                while right < _len and nums[right] == target:
                    right += 1
                return [left+1, right-1]
                # break   
        return [-1, -1]