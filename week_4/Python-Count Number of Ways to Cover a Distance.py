def count_ways_to_cover_distance(d):
    # Base cases
    if d < 0:
        return 0
    elif d == 0:
        return 1
    
    # DP array to store the number of ways to cover each distance up to d
    dp = [0] * (d + 1)
    dp[0] = 1  # There is one way to cover 0 distance: take no steps
    dp[1] = 1 
    dp[2] = 2
    dp[3] = 3
    # Fill the DP array
    for i in range(3, d + 1):
        dp[i] = dp[i - 1] + dp[i - 2]+ dp[i - 3]

    return dp[d]

if __name__=='__main__':
    # Example usage
    print(count_ways_to_cover_distance(3))  # Output: 4
    print(count_ways_to_cover_distance(4))  # Output: 7
