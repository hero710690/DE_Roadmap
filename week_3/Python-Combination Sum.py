from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtracking(remaining, combo, start):
            if remaining ==0:
                result.append(list(combo))
                return 
            elif remaining <0:
                return
            
            for i in range(start, len(candidates)):
                combo.append(candidates[i])
                backtracking(remaining-candidates[i], combo, i)
                combo.pop()
        backtracking(target, [], 0)
        return result

if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 8
    
    sol = Solution()
    sol.combinationSum(candidates, target)         
