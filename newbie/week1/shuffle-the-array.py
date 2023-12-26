class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        sl = []
        for i in range(n):
            sl.append(nums[i])
            sl.append(nums[n+i])
        return sl
        