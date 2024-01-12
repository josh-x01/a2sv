class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        if len(word1) == 0 or len(word2) == 0:
            return word1 if len(word1) > 0 else word2
        x = 0
        y = 0
        ans = []
        while x < len(word1) and y < len(word2):
            if word1[x] > word2[y]:
                ans.append(word1[x])
                x += 1
            elif word1[x] < word2[y]:
                ans.append(word2[y])
                y += 1
            else:
                temp_x = x
                temp_y = y
                for i in range(1, min(len(word1)-x, len(word2)-y) ):
                    
                    if word1[temp_x+i] > word2[temp_y+i]:
                        ans.append(word1[x])
                        x += 1
                        break
                    elif word1[temp_x+i] < word2[temp_y+i]:
                        ans.append(word2[y])
                        y += 1
                        break
                    
                else:
                    if len(word1)- x > len(word2)-y:
                        ans.append(word1[x])
                        x +=1
                    else:
                        ans.append(word2[y])
                        y += 1
        
        ans = "".join(ans)
        ans += word1[x:] + word2[y:]
        
        return ans





