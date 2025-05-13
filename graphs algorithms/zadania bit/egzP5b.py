from egzP5btesty import runtests 

def koleje ( B ):
    return sum(1 for x in find_articulation_points(to_adjlist(B)))

def to_adjlist(E):
    max_vertex = 0
    for edge in E:
        max_vertex = max(max_vertex, edge[0], edge[1])
        n = max_vertex + 1
    graph = [[] for _ in range(n)]
    for edge in E:
      graph[edge[0]].append(edge[1])
      graph[edge[1]].append(edge[0])
    return graph 

def find_articulation_points(graph):
    n = len(graph)
    disc = [-1] * n
    low = [-1] * n
    articulation = [False] * n
    id = 0

    def dfs(v, parent):
        nonlocal id, disc, low, articulation
        disc[v] = id
        low[v] = id
        id += 1
        children = 0

        for u in graph[v]:
            if disc[u] == -1:  # u is not visited yet
                children += 1
                dfs(u, v)
                low[v] = min(low[v], low[u])
                # Check if current node is an articulation point for non-root
                if parent != -1 and low[u] >= disc[v]:
                    articulation[v] = True
            elif u != parent:  # Back edge, update low[v]
                low[v] = min(low[v], disc[u])
        
        # Check if root node is an articulation point
        if parent == -1 and children >= 2:
            articulation[v] = True

    for v in range(n):
        if disc[v] == -1:
            dfs(v, -1)  # Start DFS with parent as -1 (root)

    return [i for i, is_ap in enumerate(articulation) if is_ap]

runtests ( koleje, all_tests=True )