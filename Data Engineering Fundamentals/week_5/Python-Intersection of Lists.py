# https://leetcode.com/problems/intersection-of-two-arrays/
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Convert the arrays to sets to efficiently find the intersection  
        set1 = set(nums1)  
        set2 = set(nums2)  

        # Find the intersection using the set intersection operation  
        intersection_set = set1.intersection(set2)  

        # Convert the intersection set back to a list  
        intersection_list = list(intersection_set)  

        return intersection_list  

if __name__ == '__main__':
    nums1 = [1,2,2,1]
    nums2 = [2, 2]
    sol = Solution()
    ans = sol.intersection(nums1, nums2)
    print(ans)