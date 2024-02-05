class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        out = []
        sm = sum([i for i in nums if i%2 == 0])
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                nums[idx] += val
                if nums[idx] %2 ==0:
                    sm+= val
                else :
                    sm -= nums[idx] - val
                out.append(sm)
            else :
                nums[idx] += val
                if nums[idx] %2 ==0:
                    sm+= nums[idx]
                out.append(sm)
        return (out)
    