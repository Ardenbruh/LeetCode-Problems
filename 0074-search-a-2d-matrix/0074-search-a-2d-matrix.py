class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m, n = len(matrix), len(matrix[0]) 
        t = m*n #Total number of elements
        l, r = 0, t - 1 #Setting up index l and r for binary Search 

        while l <= r:
            m = (l+r)//2
            i = m // n #to get the row index i
            j = m % n #to get the col index j 
            midNum = matrix[i][j]

            if target == midNum: return True

            elif target < midNum:
                r = m - 1

            else:
                l = m + 1

        return False

