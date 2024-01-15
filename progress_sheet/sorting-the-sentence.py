class Solution:
    def sortSentence(self, s: str) -> str:
        result = [""] * len(s.split())
        print(result)
        for ss in s.split():
            index = ss[-1]
            result[int(index)-1] = ss[:-1]
        return " ".join(result)