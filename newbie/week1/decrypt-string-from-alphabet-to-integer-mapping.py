class Solution:
    def freqAlphabets(self, s: str) -> str:
        stack = []
        word = ""
        for i in s:
            if (i =="#"):
                a = stack.pop()
                b = stack.pop()
                for j in range(len(stack)):
                    word += chr(96+int(stack[j]))
                word += chr(96+int(b+a))
                stack = []
            else:
                stack.append(i)
        for j in stack:
            word += chr(96+int(j))
        return word
        
        

         