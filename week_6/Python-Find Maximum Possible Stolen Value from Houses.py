# https://leetcode.com/problems/house-robber-ii/
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        house_num = len(nums)
        if house_num == 1:
            return nums[0]
        elif house_num == 2:
            return max(nums)
        def rob_linear(house):
            dp = [0] * len(house)
            dp[0] = house[0]
            dp[1] = max(house[0:2])
            for i in range(2, len(house)):
                dp[i] = max(dp[i-1], dp[i-2]+house[i])
            return dp[-1]
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


if __name__ == "__main__":
    nums = [2,3,2]
    sol = Solution()
    ans = sol.rob(nums) #ans =3