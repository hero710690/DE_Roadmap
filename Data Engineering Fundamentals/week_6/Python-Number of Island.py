# https://leetcode.com/problems/number-of-islands/
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        def walk(i, j):
            grid[i][j] =0
            for dr, dc in direction:
                new_i, new_j = i+dr, j+dc
                if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == '1':  
                    walk(new_i, new_j)
        
        count =0
        for r in range(m):
            for c in range(n):
                if grid[r][c]=='1':
                    count+=1
                    walk(r,c)
        return count

if __name__ == "__main__":
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    sol = Solution()
    ans = sol.numIslands(grid) #ans =1