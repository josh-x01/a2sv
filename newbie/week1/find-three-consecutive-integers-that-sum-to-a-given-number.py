class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if (num%3!=0):
            return []
        nn = num//3
        return [nn-1, nn, nn+1]