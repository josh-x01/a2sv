class Solution:
    def maxScore(self, s: str) -> int:
        zeroPrefixSum = [0]
        onePrefixSum = [0]
        _max = 0

        for i in range(len(s)):
            if s[i] == '0':
                zeroPrefixSum.append(zeroPrefixSum[i] + 1)
                onePrefixSum.append(onePrefixSum[i])
            else:
                zeroPrefixSum.append(zeroPrefixSum[i])
                onePrefixSum.append(onePrefixSum[i]+1)
        for i in range(len(s)-1):
            _max = max(_max, zeroPrefixSum[i+1] + onePrefixSum[-1] - onePrefixSum[i+1])
        print(onePrefixSum)
        print(zeroPrefixSum)
        # if s.count('0') == len(s):
        #     return _max - 1
        # else:
        return _max