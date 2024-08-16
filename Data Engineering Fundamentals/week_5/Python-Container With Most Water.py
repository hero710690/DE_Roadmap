# https://leetcode.com/problems/container-with-most-water/
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n-1
        max_water = 0
        while i<j:
            width = j-i
            current_water = min(height[i], height[j])* width
            max_water = max(max_water, current_water)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return max_water


if __name__ == "__main__":
    height = [1,8,6,2,5,4,15,3,7]
    sol = Solution()
    ans = sol.maxArea(height) #ans =49