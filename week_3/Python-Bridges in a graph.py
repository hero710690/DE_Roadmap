def find_bridges(n, connections):
    from collections import defaultdict
    
    # Create the graph
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)
    
    # Arrays to store the discovery and the lowest discovery reachable
    visited = [ False for _ in range(n)]
    bridges = []
    disc_time = [-1]*n
    lowest_disc_time = [-1]*n
    time = 0
    def dfs(u, parent):
        nonlocal time
        visited[u] = True
        disc_time[u] = lowest_disc_time[u] = time
        time+=1
        for v in graph[u]:
            print(u,v)
            if not visited[v]:
                dfs(v, u)
                lowest_disc_time[u] = min(lowest_disc_time[u], lowest_disc_time[v])
                if lowest_disc_time[v] > disc_time[u]:
                    bridges.append((u,v))

            elif v!=parent:
                lowest_disc_time[u] = min(lowest_disc_time[u], lowest_disc_time[v])
                
    # Call DFS from the first vertex (assuming graph is connected)
    for i in range(n):
        if not visited[i]:
            dfs(i, -1)
    return bridges

# Example usage
n = 5  # Number of vertices
connections = [(1, 0), (0, 2), (2, 1), (0, 3), (3, 4)]
print(find_bridges(n, connections))