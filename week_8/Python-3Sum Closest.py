# https://leetcode.com/problems/3sum-closest/
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        delta = float('inf')
        result = 0
        if len(nums) <=3:
            return sum(nums)
        for i in range(n-2):
            if i> 0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j < k:
                total = nums[i]+nums[j]+nums[k]
                if total==target:
                    return target
                elif abs(total- target) < delta:
                        delta = abs(target-total)
                        result = total
               
                if total>target:
                    k-=1
                else:
                    j+=1
                
        return result
    
if __name__ == "__main__":
    sol = Solution()
    def test_threeSumClosest():
        assert sol.threeSumClosest([-1,2,1,-4], 1) == 2, " test 1 passed"
        assert sol.threeSumClosest([0,0,0],0) == 0, "test 2 passed"
        assert sol.threeSumClosest([10,9,2,-5, 0, 0,-3,7,101,-18], 1) == 1, "test 3 passed"
        print("All test cases passed!")
    test_threeSumClosest()