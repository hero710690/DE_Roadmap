from collections import deque
from typing import List
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)  
        def get_s(idx):
            # Get the row and column from the index
            r, c = divmod(idx-1, n)
            if r % 2 == 1:
                c = n - 1 - c
            return n - 1 - r, c

        queue = deque([(1, 0)])  # (current square, number of moves)
        visited = set([1])
        
        while queue:
            s, moves = queue.popleft()
            if s == n * n:
                return moves
            for next_s in range(s + 1, min(s + 6, n * n) + 1):
                nr, nc = get_s(next_s)
                if board[nr][nc] != -1:
                    next_s = board[nr][nc]
                if next_s not in visited:
                    visited.add(next_s)
                    queue.append((next_s, moves + 1))
        
        return -1



if __name__ == "__main__":
    board = [[-1,-1,19,10,-1],[2,-1,-1,6,-1],[-1,17,-1,19,-1],[25,-1,20,-1,-1],[-1,-1,-1,-1,15]]
    sol = Solution()
    ans = sol.snakesAndLadders(board) #ans =2