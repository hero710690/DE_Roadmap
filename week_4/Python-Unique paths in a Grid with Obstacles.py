class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        dp[0][0] = 1
        if obstacleGrid[0][0] == 1:
            return 0
        for i in range(1, row):
            if obstacleGrid[i][0]==0:
                dp[i][0] = dp[i-1][0]
        
                
        for j in range(1, col):
            if obstacleGrid[0][j]==0:
                dp[0][j] = dp[0][j-1]


        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j]==0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[row-1][col-1]
    
if __name__ == '__main__':
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    sol = Solution()
    ans = sol.uniquePathsWithObstacles(obstacleGrid) #ans =2