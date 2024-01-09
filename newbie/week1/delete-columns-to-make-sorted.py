class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        total = 0
        cols = []
        for i in range(len(strs[0])):
            sub_col = []
            for j in range(len(strs)):
                sub_col.append(strs[j][i])
            cols.append(''.join(sub_col))
        print(cols)
        for _str in cols:
            ord_str = [ord(s) for s in _str]
            if ord_str != sorted(ord_str):
                total += 1
        return total
            