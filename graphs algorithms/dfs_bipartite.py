 
graph = [
    [3, 4],  # 0 → 3, 4
    [4, 5],  # 1 → 4, 5
    [3, 5],  # 2 → 3, 5
    [0, 2],  # 3 → 0, 2
    [0, 1],  # 4 → 0, 1
    [1, 2]   # 5 → 1, 2
]
  
def is_bipartie(graph):        
    color = [-1 for i in range(len(graph))]

    def visit_node(u, c):
        nonlocal color
        nonlocal graph
        color[u] = c
        for v in graph[u]:
            if color[u]  == color[v]:
                return False
            if color[v] ==-1:
                if not visit_node(v, 1 - c):
                    return False
        return True 
    
    for v in range(len(graph)):
        if color[v] == -1:
            if not visit_node(v,0):
                return False
    return True

print(is_bipartie(graph))