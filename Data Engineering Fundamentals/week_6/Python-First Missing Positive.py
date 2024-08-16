# https://leetcode.com/problems/first-missing-positive/
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <=n and nums[nums[i]-1] !=nums[i]:
                correct_index = nums[i] - 1  
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
        for i in range(n):
            if nums[i]!= i +1:
                return i+1
        return n+1

if __name__ == '__main__':
    nums = [3,2,-1,0,4]
    sol = Solution()
    ans = sol.firstMissingPositive(nums) #ans = 1
        