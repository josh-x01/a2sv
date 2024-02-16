class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = defaultdict(lambda: 0)

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temperatures[i], i))
        print(res)
        return [ res[temp] for temp in range(len(temperatures))] 