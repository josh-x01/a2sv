class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pl = []
        nl = []
        for i in nums:
            if (i < 0):
                nl.append(i)
            else:
                pl.append(i)
        al = []
        for i in range(len(pl)):
            al.append(pl[i])
            al.append(nl[i])
        return al