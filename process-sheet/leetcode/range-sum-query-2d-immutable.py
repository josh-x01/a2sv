class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixSum = []
        for i in range(len(matrix)+1):
            self.prefixSum.append([0]*(len(matrix[0])+1))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.prefixSum[i+1][j+1] = matrix[i][j] + self.prefixSum[i+1][j] + self.prefixSum[i][j+1] -self.prefixSum[i][j] 
        print(self.prefixSum)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        row2 += 1
        col1 += 1
        col2 += 1
        # print(self.prefixSum[row2][col2], self.prefixSum[row1-1][col2], self.prefixSum[row2][col1-1], self.prefixSum[row1-1][col1-1])
        return self.prefixSum[row2][col2] - self.prefixSum[row1-1][col2] - self.prefixSum[row2][col1-1] + self.prefixSum[row1-1][col1-1] 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)