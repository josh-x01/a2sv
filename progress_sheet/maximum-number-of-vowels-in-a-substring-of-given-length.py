class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        r = k
        initVol = 0
        vol = {'a', 'e', 'i', 'o', 'u'}
        for i in range(k):
            if s[i] in vol:
                initVol += 1
        curVol = maxVol = initVol

        for i in range(len(s)-k):
            # print('l:', s[l+i], 'r:', s[r+i])
            if s[l+i] in vol:
                curVol -= 1
            if s[r+i] in vol:
                curVol += 1
            maxVol = max(curVol, maxVol)
        return maxVol
            