# https://leetcode.com/problems/longest-increasing-subsequence/
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp  = [ 1 for _ in range(len(nums))]
        curr_min = float('inf')
        curr_max = float('-inf')
        for i in range(len(nums)):
            for j in range(i): 
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

if __name__ == "__main__":
    sol = Solution()
    def test_llengthOfLIS():
        assert sol.lengthOfLIS([7,7,7,7,7,7,7]) == 1, " test 1 passed"
        assert sol.lengthOfLIS([0,1,0,3,2,3]) == 4, "test 2 passed"
        assert sol.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4, "test 3 passed"
        print("All test cases passed!")
    test_llengthOfLIS()