class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n = len(flips)
        checked = []
        n = 0
        max_ = float("-inf")
        c = 0
        for i in flips:
            if i > max_:
                max_ = i
            checked.append(i)
            n+=1
            if max_ == n:
                c+=1
        return (c)