class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_dict = Counter(nums)
        return [k for k, v in nums_dict.items() if v == 2]