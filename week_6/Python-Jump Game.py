# https://leetcode.com/problems/jump-game/
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i in range(len(nums)):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i+nums[i])
            if maxReach>=len(nums)-1:
                return True
        return False

if __name__ == '__main__':
    nums = [3,2,1,0,4]
    sol = Solution()
    ans = sol.canJump(nums) #False
        