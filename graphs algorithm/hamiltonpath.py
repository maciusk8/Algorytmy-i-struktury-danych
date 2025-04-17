dag = [
    [1, 2],    # wierzchołek 0 ma krawędzie do 1 i 2
    [3],       # wierzchołek 1 ma krawędź do 3
    [3, 4],    # wierzchołek 2 ma krawędzie do 3 i 4
    [5],       # wierzchołek 3 ma krawędź do 5
    [5],       # wierzchołek 4 ma krawędź do 5
    []         # wierzchołek 5 nie ma wychodzących krawędzi
]
hamilton = [
    [1, 2],    # 0 -> 1, 2
    [2, 3],    # 1 -> 2, 3
    [3, 4],    # 2 -> 3, 4
    [4, 5],    # 3 -> 4, 5
    [5],       # 4 -> 5
    []         # 5 -> []
]

def h_path(graph):
    n = len(graph)
    ts = []
    visited = [False for i in range(n)]

    def visit(v):
        nonlocal n,graph,visited
        visited[v] = True
        for u in graph[v]:
            if not visited[u]:
                visit(u)
        ts.append(v)

    for v in range(n):
        if not visited[v]:
            visit(v)

    ts = ts[::-1]
    for i in range(n-1):
        flag = False
        for u in graph[ts[i]]:
            if u == ts[i+1]:
                flag = True
        if not flag:
            return -1
    return ts

print(h_path(dag))
    
        