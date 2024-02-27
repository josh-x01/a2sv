class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                gen_s = []
                while stack and stack[-1] != '[':
                    gen_s.append(stack.pop())
                
                stack.pop()
                gen_num = []
                nums = '1234567890'
                while stack and stack[-1] in nums:
                    gen_num.append(stack.pop())
                gen_s.reverse()
                gen_num.reverse()
                gen_s = gen_s * int(''.join(gen_num))
                stack = stack + gen_s
        # print(stack)
        return ''.join(stack)