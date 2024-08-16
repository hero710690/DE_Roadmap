from typing import List
class Solution:
    def cuttingRod(self, prices:List, rodLenght: int) -> int:
        dp = (rodLenght+1) * [0]
        for i in range(1, rodLenght+1):
            for j in range(rodLenght-i,0, -1):
                
                dp[j] = prices[i-1] + prices[j-1]
                
            dp[i] = max(dp[j], dp[j-i], prices[i-1])
         
        return dp[rodLenght]

if __name__ == "__main__":
    rodLenght = 4
    prices = [1, 2, 3, 4]
    sol = Solution()
    def test_cutRod():
        assert sol.cuttingRod([1, 2, 3, 4], 4) == 4, "Test Case 1 Failed"
        assert sol.cuttingRod([2, 5, 7, 8, 10], 5) == 12, "Test Case 2 Failed"
        assert sol.cuttingRod([1, 1, 1, 10, 10, 15, 17, 20, 24, 30], 10) == 30, "Test Case 3 Failed"
        print("All test cases passed!")

    test_cutRod()
