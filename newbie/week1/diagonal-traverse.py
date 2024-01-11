class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        hash = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i+j in hash.keys():
                    hash[i+j] = hash[i+j] + [mat[i][j]]
                else:
                    hash[i+j] = [mat[i][j]]
        result = []
        for k, v in hash.items():
            if k%2 == 0:
                v.reverse()
                result.extend(v)
            else:
                result.extend(v)
        return result
        