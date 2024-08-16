from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        visited = []
        while left < right and top < bottom:
            
            for i in range(left, right):
                visited.append(matrix[top][i])
            top+=1
            for j in range(top, bottom):
                
                visited.append(matrix[j][right-1])
            right-=1
            if not (left < right and top < bottom):
                break
            for i in range(right-1, left-1, -1 ):
                visited.append(matrix[bottom-1][i])
            bottom-=1
            print(bottom, left)
            for j in range(bottom-1,top-1, -1):
                print(j)
                visited.append(matrix[j][left])
            left+=1


        return visited


matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
ans = sol.spiralOrder(matrix)
print(ans)