class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = defaultdict(lambda: -1)

        for num in nums2:
            while stack and stack[-1] < num:
                res[stack[-1]] = num
                stack.pop()
            stack.append(num)
        return [ res[num] for num in nums1]





        # stack = []
        # pair = {}
        # for i in range(len(num2)):
        #     if not stack and nums[i] < stack[-1]:
        #         stack.append(num2[i])
        #         continue
        #     pair[]
            
