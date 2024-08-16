# https://leetcode.com/problems/flood-fill/
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        color_center = image[sr][sc]
        def dfs(r, c):
            if c < 0 or c >= len(image[0]): return
            if r  < 0  or r >= len(image): return
            
            if image[r][c]==color: return 
            if image[r][c]!=color_center: return
            
            image[r][c] = color
            
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        dfs(sr, sc)
        return image
    
if __name__ == "__main__":
    sol = Solution()
    def test_floodFill():
        assert sol.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2) == [[2,2,2],[2,2,0],[2,0,1]], "Test Case 1 Failed"
        assert sol.floodFill([[0,0,0],[0,0,0]],0,0,0) == [[0,0,0],[0,0,0]], "Test Case 2 Failed"
        assert sol.floodFill([[0,0,0],[0,0,0]],1,0,2) == [[2,2,2],[2,2,2]], "Test Case 3 Failed"
        print("All test cases passed!")
    test_floodFill()
