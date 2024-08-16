nums = [-2,1,-3,4,-1,2,1,-5,4]

# using Kadane's Algorithm
def maxSubarray(arr):
    if not arr:
        return 0
    max_subarray = current_subarray = arr[0]

    for i in range(1, len(arr)):
        current_subarray = max(arr[i], current_subarray+arr[i])
        max_subarray = max(max_subarray, current_subarray)

    return max_subarray