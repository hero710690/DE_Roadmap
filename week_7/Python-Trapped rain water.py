# https://leetcode.com/problems/trapping-rain-water/
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        vol = 0
        left = 0
        right = len(height)-1
        left_max, right_max = 0, 0  
        while left < right:

            if height[right]>=height[left]:
                if height[left]<left_max:
                    vol+= left_max - height[left]
                else:
                    left_max = height[left]
                left+=1
            if height[right] < height[left]:
                if height[right]<right_max:
                    vol+= right_max - height[right]
                else:
                    right_max = height[right]
                right-=1
        return vol
if __name__ == "__main__":
    sol = Solution()
    def test_trap():
        assert sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6, "Test Case 1 Failed"
        assert sol.trap([4,2,0,3,2,5]) == 9, "Test Case 2 Failed"
        assert sol.trap([4,2,3]) == 1, "Test Case 3 Failed"
        print("All test cases passed!")
    test_trap()
    

            

        