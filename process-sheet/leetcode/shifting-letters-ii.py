class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        length = len(s)
        total = [0] * (length + 1)
        for shift in shifts:
            start = shift[0]
            end = shift[1]
            op = shift[2]
            if op == 0:
                total[start] -= 1
                total[end+1] += 1
            else:
                total[start] += 1
                total[end+1] -= 1
        prefix = [0]
        for t in total:
            prefix.append(prefix[-1] + t)
        ans = []
        print(prefix)
        for i in range(length):
            result = ord(s[i]) + (prefix[i+1] % 26)
            if 97 <= result <= 122:
                ans.append(chr(result))
            elif result < 97:
                ans.append(chr(122 - (96 - result)))
            else:
                ans.append(chr(97 + (result - 123)))
        return "".join(ans)