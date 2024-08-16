from typing import List
import numpy as np

## Leetcode Easy Example
class Solution:
    def twoSumPointer(self, nums: List[int], target: int) -> List[int]:
        sorted_index = list(np.argsort(nums))
        l, r = 0, len(nums)-1
        while l < r:
            print(l, r)
            print(nums[sorted_index[l]], nums[sorted_index[r]])
            if nums[sorted_index[l]]+ nums[sorted_index[r]] == target:
                return [sorted_index[l], sorted_index[r]]
            elif abs(nums[sorted_index[l]] + nums[sorted_index[r]]) < target or nums[sorted_index[l]] + nums[sorted_index[r]] < target:
                l+=1
            else:
                r-=1
        
    def twoSumHash(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            
            if num in hash_map:
                return [hash_map[num],i]
            hash_map[target - num] = i
            
nums = [0,3,-3,4,-1]
target = -1
sol = Solution()
# ans1 = sol.twoSumPointer(nums, target)
ans2 = sol.twoSumHash(nums, target)
print(ans2)