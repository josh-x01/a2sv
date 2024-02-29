class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backt(path):
            if len(path) == len(nums):
                res.append(list(path))
                return
            if len(path)>= len(nums):
                return 
            for i in range(len(nums)):
                if nums[i] not in path:
                    print(path)
                    path.append(nums[i])
                    backt(path)
                    path.pop()
        backt([])
        return res