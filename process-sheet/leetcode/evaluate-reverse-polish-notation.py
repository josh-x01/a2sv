class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lis = []
        for i in range(len(tokens)):
            if tokens[i] not in "+*/-"  :
                lis.append(int(tokens[i]))
            else:
                x = lis.pop()
                y = lis.pop()
                if tokens[i] == "+":
                    lis.append(x + y)
                elif tokens[i] == "-":
                    lis.append(y - x)
                elif tokens[i] == "*":
                    lis.append(x * y)
                elif tokens[i] == "/":
                    lis.append(int(y / x))
        return lis[0]