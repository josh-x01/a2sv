class NumArray:

    def __init__(self, nums: List[int]):
        self.lis = [0]
        for i in range(len(nums)):
            self.lis.append(self.lis[i] + nums[i])
    def sumRange(self, left: int, right: int) -> int:
        return self.lis[right+1] - self.lis[left]