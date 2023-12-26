class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            length=min(len(w1), len(w2))
            for j in range(length):
                i1 = order.index(w1[j])
                i2 = order.index(w2[j])
                if (i1 > i2):
                    return False
                elif (i1 < i2):
                    break
                else:
                    if (j+1 == length):
                        if (len(w1) > len(w2)):
                            return False
                    continue
        return True

