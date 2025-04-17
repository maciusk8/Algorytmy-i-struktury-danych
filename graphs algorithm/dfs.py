#dfs 
graph = [
    [3, 4],  # 0 → 3, 4
    [4, 5],  # 1 → 4, 5
    [3, 5],  # 2 → 3, 5
    [0, 2],  # 3 → 0, 2
    [0, 1],  # 4 → 0, 1
    [1, 2]   # 5 → 1, 2
]
  
def dfs(graph):        
    visited = [False for i in range(len(graph))]

    def visit_node(u):
        nonlocal visited
        nonlocal graph
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                visit_node(v)
    
    for v in range(len(visited)):
        if visited[v] == False:
            visit_node(v)
