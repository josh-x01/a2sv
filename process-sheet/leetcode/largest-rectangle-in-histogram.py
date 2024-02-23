class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        length = len(heights)
        area = 0
        for i in range(length):
            # print(stack)
            index = i
            while stack and stack[-1][0] > heights[i]:
                temp, indx = stack.pop()
                area = max(area, (temp * (i - indx)))
                index = indx
            # print(index)
            stack.append((heights[i], index))

        l = len(heights)
        while stack:
            temp = stack.pop()
            area = max(area, (temp[0] * (l - temp[1])))
        
        return area