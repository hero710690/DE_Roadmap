# https://leetcode.com/problems/coin-change/
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        max_value = amount + 1
        dp = [max_value] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin]+1)

        return dp[amount] if dp[amount]!=max_value else -1

if __name__ == "__main__":
    coins = [1,2,5]
    amount = 11
    sol = Solution()
    ans = sol.coinChange(coins, amount) # ans = 11