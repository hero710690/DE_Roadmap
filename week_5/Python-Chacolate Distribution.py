# https://leetcode.com/problems/fair-distribution-of-cookies/
from typing import List
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)  
        # Initialize an array to hold the total cookies for each child  
        children = [0] * k  
        min_unfairness = float('inf')  
        
        # Backtracking function  
        def backtrack(i):  
            nonlocal min_unfairness  
            if i == n:  # All cookie bags have been assigned  
                max_cookies = max(children)  # Calculate unfairness  
                min_unfairness = min(min_unfairness, max_cookies)  
                return  
            
            for j in range(k):  
                children[j] += cookies[i]  # Assign current cookie bag to j-th child  
                backtrack(i + 1)  # Move to the next cookie bag  
                children[j] -= cookies[i]  # Undo the assignment  
                
                # Pruning: If the current child already has max_cookies >= min_unfairness, skip  
                if children[j] >= min_unfairness:  
                    break  

        # Start backtracking from the first cookie bag  
        backtrack(0)  
        return min_unfairness  


if __name__ == "__main__":
    cookies = [8,15,10,20,8]
    k = 2
    sol = Solution()
    ans = sol.distributeCookies(cookies, k) #ans =31