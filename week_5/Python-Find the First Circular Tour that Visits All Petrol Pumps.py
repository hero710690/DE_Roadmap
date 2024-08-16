# https://leetcode.com/problems/gas-station/
from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_station = 0
        current_tank, total_tank = 0, 0 
        for i in range(len(gas)):
            current_tank += gas[i]-cost[i]
            total_tank += gas[i]-cost[i]

            if current_tank<0:
                start_station = i+1
                current_tank = 0
        return start_station if total_tank >= 0 else -1
    
if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    sol = Solution()
    ans = sol.canCompleteCircuit(gas, cost)
