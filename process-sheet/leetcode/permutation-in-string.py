class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left,  right = len(s1), len(s2)
        if left>right:
            return False
        cout_1, cout_2 = Counter(s1), Counter(s2[:left])
        for i in range(right - left):
            if cout_1 == cout_2:
                return True
            char_1, char_2 = s2[i], s2[i+left]
            cout_2[char_1] -=1
            if cout_2[char_1] == 0:
                del cout_2[char_1]
            cout_2[char_2] +=1
        return cout_1 == cout_2