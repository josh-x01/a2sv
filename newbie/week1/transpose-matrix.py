class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(matrix[0])):
            sub_arr = []
            for j in range(len(matrix)):
                sub_arr.append(matrix[j][i])
            result.append(sub_arr)
        return result