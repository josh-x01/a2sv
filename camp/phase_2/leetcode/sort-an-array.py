class Solution:
    def comb(self, left, right):
        ans = []
        l, r = 0, 0 
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ans.append(left[l])
                l += 1
            else:
                ans.append(right[r])
                r += 1
        ans.extend(left[l:])
        ans.extend(right[r:])
        return ans

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) in [0, 1]:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.comb(left, right)

