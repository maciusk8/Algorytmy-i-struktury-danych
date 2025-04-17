from queue import Queue
#bfs sprawdzanie czy graf jest spojny
graph = [
    [1, 2],       # 0 → 1, 2
    [0, 3, 4],    # 1 → 0, 3, 4
    [0, 5, 6],    # 2 → 0, 5, 6
    [1],          # 3 → 1
    [1, 7],       # 4 → 1, 7
    [2],          # 5 → 2
    [2, 8],       # 6 → 2, 8
    [4],          # 7 → 4
    [6]           # 8 → 6
]
"""
      0
    /   \.
   1     2
  / \   / \.
 3   4 5   6
      \   /
       7 8 
"""

def bfs(Graph):
    l = len(graph)
    visited = [False for i in range(l)]
    q = Queue()
    q.put(0)
    while not q.empty():
        v = q.get()
        if not visited[v]:
            for w in graph[v]:
                q.put(w)
        visited[v] = True
    return is_connected(visited)

def is_connected(visited):
    for v in visited:
        if v == False:
            return v
    return True

print(bfs(graph))


