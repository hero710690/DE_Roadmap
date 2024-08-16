# The isBadVersion API is already defined for you.
#https://leetcode.com/problems/first-bad-version/
bad = 4
def isBadVersion(version: int) -> bool:
    return version==bad
class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left, right = 1, n  
    
        while left < right:  
            mid = left + (right - left) // 2  
            if isBadVersion(mid):  
                right = mid  
            else:  
                left = mid + 1  
        
        return left  

if __name__ == "__main__":
    n = 5
    sol = Solution()
    ans = sol.firstBadVersion(n)