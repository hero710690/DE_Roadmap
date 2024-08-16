# https://leetcode.com/problems/transpose-matrix/
from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        transposed = [ [0 for _ in range(m) ] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                transposed[j][i] = matrix[i][j]
        return transposed
if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol = Solution()
    ans = sol.transpose(matrix) #[[1,4,7],[2,5,8],[3,6,9]]
    