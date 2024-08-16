from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        overlap = []
        intervals.append(newInterval)
        intervals.sort()
        for interval in intervals:
            if not overlap or interval[0]>overlap[-1][1]:
                overlap.append(interval)
            else:
                overlap[-1][1] = max(interval[1], overlap[-1][1])
            
        return overlap


if __name__ == '__main__':
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    sol = Solution()
    ans = sol.insert(intervals, newInterval)