class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        sal = salary[1:-1]
        return sum(sal)/len(sal)
        