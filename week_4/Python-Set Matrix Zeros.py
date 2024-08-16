class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False

        # Check if the first row contains zero
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
        
        # Check if the first column contains zero
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
    
        # Mark zeros in the first row and first column
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Set zeros based on markings in the first row and first column
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Set zeros in the first row
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0
        
        # Set zeros in the first column
        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0

if __name__=='__main__':
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    sol = Solution()
    ans = sol.setZeroes(matrix)
    print(matrix) #[[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]