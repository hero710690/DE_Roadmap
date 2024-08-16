class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
    
        # Base condition: There is one way to achieve target sum 0 with 0 dice: use no dice
        dp[0][0] = 1
        
        # Fill the DP table
        for i in range(1, n + 1):        # For each die
            for j in range(1, target + 1):  # For each target sum from 1 to target
                dp[i][j] = 0
                for face in range(1, k + 1):  # For each face of the die
                    if j >= face:
                        dp[i][j] += dp[i - 1][j - face]
                        dp[i][j] %=( 10**9 + 7 )

        return dp[n][target]


if __name__ == '__main__':
 n = 2
 k = 6
 target = 7
 sol = Solution()
 ans = sol.numRollsToTarget(n, k, target) # 6