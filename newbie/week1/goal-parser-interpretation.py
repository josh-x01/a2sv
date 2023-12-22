class Solution:
    def interpret(self, command: str) -> str:
        c = ""
        cc = ""
        for i in command:
            cc += i
            if (i == 'G'):
                c += 'G'
                cc = ""
                continue
            if (cc == '(al)'):
                c += 'al'
                cc = ""
                continue
            if (cc == '()'):
                c += 'o'
                cc = ""
                continue
        return c
            