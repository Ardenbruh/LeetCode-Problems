class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        # """
        # m, n = len(matrix), len(matrix[0])
        # r, l = False, False

        # for j in range(n):
        #     if matrix[0][j] == 0:
        #         r = True
        #         break
        # for i in range(m):
        #     if matrix[i][0] == 0:
        #         l = True 
        #         break

        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             matrix[0][j] = 0
        #             matrix[i][0] = 0

        # for i in range(1, m):
        #     if matrix[i][0] == 0:
        #         for j in range(1,n):
        #             matrix[i][j] = 0

        # for j in range(1, n):
        #     if matrix[0][j] == 0:
        #         for i in range(1, m):
        #             matrix[i][j] = 0            
            
        # if l:
        #     for i in range(m):
        #         matrix[i][0] = 0
        # if r:
        #     for j in range(n):
        #         matrix[0][j] = 0

        # # I will forget this for sure. 
        
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0 
                    matrix[0][j] = 0  
        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
