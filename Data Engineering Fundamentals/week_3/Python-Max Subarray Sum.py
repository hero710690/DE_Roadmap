
def maxSubarraySum(nums):
    current_max = nums[0]
    max_sum = nums[0]
    for i in range(1, len(nums)):
        current_max = max(nums[i], current_max+nums[i])
        max_sum = max(max_sum,current_max)
    return max_sum
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = maxSubarraySum(nums)