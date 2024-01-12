class Solution:
    def maxArea(self, height: List[int]) -> int:
        x = 0
        y = len(height)-1
        ans = 0
        while(x<y):
            sum_of = (min(height[x],height[y]) * (y-x))
            ans = max(ans,sum_of)
            if height[x] < height[y]:
                x +=1
            else:
                y -= 1
        return ans
        