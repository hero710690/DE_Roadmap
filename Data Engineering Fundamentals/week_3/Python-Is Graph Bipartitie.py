from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for _ in range(len(graph))]

        def dfs(node, c):
            color[node] = c
            for neighbor in graph[node]:
                if color[neighbor]==c:
                    return False
                if color[neighbor] == -1 and not dfs(neighbor, 1-c):
                    return False
            return True
        for node in range(len(graph)):
            if color[node] == -1 and not dfs(node,0):
                return False
        return True 

if __name__ == '__main__':
    graph = [[2,4],[2,3,4],[0,1],[1],[0,1],[7],[9],[5],[],[6],[12,14],[],[10],[],[10],[19],[18],[],[16],[15],[23],[23],[],[20,21],[],[],[27],[26],[],[],[34],[33,34],[],[31],[30,31],[38,39],[37,38,39],[36],[35,36],[35,36],[43],[],[],[40],[],[49],[47,48,49],[46,48,49],[46,47,49],[45,46,47,48]]
    sol = Solution()
    ans = sol.isBipartite(graph)
    print(ans)