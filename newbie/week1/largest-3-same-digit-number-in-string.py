class Solution:
    def largestGoodInteger(self, num: str) -> str:
        stack = []
        checked = []
        for i in range(len(num)):
            if (len(stack) == 0):
                stack.append(num[i])
                continue
            if (len(stack) == 3):
                checked.append(stack[-1])
                stack = []
                stack.append(num[i])
                continue
            if (num[i] != stack[-1]):
                stack = []
                stack.append(num[i])
                continue
            stack.append(num[i])
            print(stack)
        if (len(stack) == 3):
            checked.append(stack[-1])
        if (len(checked) == 0):
            return ""
        _max = max(checked)
        return str(_max) * 3