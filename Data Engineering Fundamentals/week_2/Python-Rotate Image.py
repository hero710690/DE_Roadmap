from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]
        for i in range(len(matrix)):
            matrix[i].reverse()
        
if __name__=='__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol = Solution()
    sol.rotate(matrix=matrix)
    print(matrix)
