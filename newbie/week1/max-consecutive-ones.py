class Solution:
    def findMaxConsecutiveOnes(self, nums):
        m1 = 0
        mc = 0
        for i in nums:
            if (i == 1):
                mc += 1
            else:
                m1 = max(mc, m1)
                mc = 0
        return max(m1, mc)