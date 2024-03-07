class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        def magic(start,path):
            if start==len(nums):
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                magic(i+1, path)
                x = sorted(path[:])
                if not x  in ans:
                    ans.append(x)
                path.pop()

        magic(0,[])

        return ans