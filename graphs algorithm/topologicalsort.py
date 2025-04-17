graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['G', 'H'],
    'E': [],
    'F': ['I', 'J'],
    'G': ['K'],
    'H': [],
    'I': [],
    'J': ['K'],
    'K': []
}

def dfs(graph):
    visited = dict.fromkeys(graph.keys(), False)
    ts = []

    def visit(v):
        visited[v] = True
        neighbours = graph[v]
        for u in neighbours:
            if not visited[u]:
                visit(u)
        ts.append(v)

    for v in graph.keys():
        if not visited[v]:
            visit(v)

    return ts[::-1]

print(dfs(graph))   

    
