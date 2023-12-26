class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        start = 1
        for i in range(n//7):
            total += ((7/2) * (2*start + 6))
            start += 1
            print(total, end=" ")
        total += (n%7)/2 * (2*start + n%7-1)
        return int(total)