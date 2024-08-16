#http://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = -float('inf')
        for price in prices:
            if price< minPrice:
                minPrice = price
            if price - minPrice > maxProfit:
                maxProfit = price - minPrice
        return maxProfit


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    sol = Solution()
    ans = sol.maxProfit(prices) #ans=5
    print(ans)