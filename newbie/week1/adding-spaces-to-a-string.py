class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        space_set = set(spaces)
        for i in range(len(s)):
            if i in space_set:
                result.append(' ')
            result.append(s[i])
        return "".join(result)