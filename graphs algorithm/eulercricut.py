macierz_sasiedztwa = [
    [0, 1, 1],  # Wierzchołek 0 połączony z 1 i 2
    [1, 0, 1],  # Wierzchołek 1 połączony z 0 i 2
    [1, 1, 0]   # Wierzchołek 2 połączony z 0 i 1
]

# Inny przykład - graf z cyklem Eulera ale nie pełny
macierz_sasiedztwa_2 = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0]
]

def dfs(G):
    n = len(G)
    parent = [None for _ in range(n)]
    U = [0 for _ in range(n)]
    cycle = []

    def dfs_visit(G, v):
        nonlocal parent, n, cycle, U
        p = parent[v]
        if p != None:
            G[v][p] = G[p][v] = 0
        while U[v] < n:
            u = U[v]; U[v] += 1
            if G[v][u] == 1:
                parent[u] = v
                dfs_visit(G, u)
        cycle.append(v)

    dfs_visit(G, 0)
    
    return cycle
