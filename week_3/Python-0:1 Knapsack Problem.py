
"""
Problem Statement:
Given:

A set of n items numbered from 1 up to n.
Each item has a weight w[i] and a value v[i].
A maximum weight capacity of the knapsack W.
Find the maximum value V that can be achieved by packing items in the knapsack such that the total weight does not exceed W.

"""
def knapsack(W, weigths, values, n):

    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(1, n+1):
        for j in range(W+1):
            if weights[i-1]<=j:
                dp[i][j] = max(dp[i-1][j], values[i-1]+dp[i-1][j-weights[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][W]



if __name__ == '__main__':
    values = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50
    n = len(values)
    print(knapsack(W, weights, values, n))