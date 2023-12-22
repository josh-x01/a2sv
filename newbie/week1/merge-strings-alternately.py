class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = ""
        m1 = ""
        m2 = ""
        i1 = 0
        i2 = 0
        turn = 0
        l = len(word1) + len(word2)
        for i in range(300):
            if (i1+1 <= len(word1)):
                if (turn == 0):
                    m += word1[i1]
                    m1 += word1[i1]
                    i1+=1
                    turn = 1
                    continue
            else:
                turn = 1
            if (i2+1 <= len(word2)):
                if (turn == 1):
                    m += word2[i2]
                    m2 += word2[i2]
                    i2+=1
                    turn = 0
                    continue
            else:
                turn = 0
        return m
                