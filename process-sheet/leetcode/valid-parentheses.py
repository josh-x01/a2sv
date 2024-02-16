class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s) <= 1:
        #     return False
        open_brack = ['(', '[', '{']
        close_brack = [')', ']', '}']
        stack = []
        for bracket in s:
            # print(stack)
            if bracket in open_brack:
                stack.append(bracket)
                continue
            if len(stack) == 0:
                return False
            index = close_brack.index(bracket)
            if stack[-1] == open_brack[index]:
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True