class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mc = 0
        for i in candies:
            mc = max(mc, i)
        gc = []
        for i in candies:
            gc.append(i+extraCandies >= mc)
        return gc