graph = [
    [(1, 3), (2, 5), (3, 2)],          # 0
    [(4, 7), (5, 1)],                   # 1
    [(1, 2), (3, 4), (6, 6)],           # 2
    [(6, 3), (7, 8)],                   # 3
    [(5, 2), (8, 4)],                   # 4
    [(8, 3), (9, 5)],                   # 5
    [(7, 1), (9, 7)],                   # 6
    [(9, 2)],                           # 7
    [(9, 6)],                           # 8
    []                                  # 9
]

from queue import PriorityQueue 

def dijkstra(G, s):
    n = len(G)
    d = [float('inf')]*n
    d[s] = 0
    visited = [False]*n
    q = PriorityQueue()
    q.put((0,s))
    while not q.empty():
        v = q.get()[1]
        if not visited[v]:
            for u, wu in graph[v]:
                if d[v] + wu < d[u]:
                    d[u] = d[v] + wu
                q.put((d[u], u))
        visited[v] = True
    return d

print(dijkstra(graph, 0))