class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n, m, l = len(board), len(board[0]), len(word)
        # row and col operations to traverse vertially and horizontally
        direc = [(1,0), (0,1), (-1,0), (0,-1)]
        # to track visited cells to not revisited them again other wise it's going to endup inf 
        visited = set()
        
        # invalid basecase
        def inBound(row, col, indx):
            if 0 <= row < n and 0 <= col < m and (row, col) not in visited and board[row][col] == word[indx]:
                return True 
        
        def backtrack(row, col, indx):
            # valid basecase
            if indx == l:
                return True
            # marked the current cell visited
            visited.add((row, col))
            for i, j in direc:
                # forming new path
                newRow = row + i
                newCol = col + j
                # check if it is in the base constraints
                if inBound(newRow, newCol, indx):
                    # check we found the correct path
                    if backtrack(newRow, newCol, indx + 1):
                        return True
            # removing the visited cell during back propagation
            visited.remove((row, col))
            
        # considering every cell as a starting point
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 1):
                        return True









# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         word_len = len(word)
#         row_len = len(board[0])
#         col_len = len(board)
#         visited = set()

#         def backtrack(row: int, col: int, index: int = 0):
#             if (row, col) in visited:
#                 return
#             if (row < 0 or row >= row_len) or (col < 0 or col >= col_len):
#                 return
#             if index > word_len:
#                 return False
#             if index == word_len and :
#                 return True

#             visited.add((row, col))
#             moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
#             for r_mv, c_mv in moves:
#                 if backtrack(row + r_mv, col + c_mv, index+1):
#                     return True
#             print(word[index], end=" ")

#         return backtrack(0, 0)
