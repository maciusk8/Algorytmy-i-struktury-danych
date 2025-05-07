#algorytm szukania krawdzi bedacymi mostami w grafie
graph = [[1,2],[0,2,3],[1,0],[1]]

def find_bridges(G):
    n = len(G)
    d = [-1] * n       
    low = [-1] * n     
    bridges = []
    time = 0

    def dfs(v, p=-1):
        nonlocal time, d, low, bridges
        d[v] = low[v] = time 
        time += 1
        for u in G[v]: 
            if u == p: 
                continue
            else: 
                if d[u] == -1: 
                    dfs(u, v)
                low[v] = min(low[v], low[u])
                if low[u] > d[v]:
                    bridges.append((v, u))

    for v in range(n):
        if d[v] == -1:
            dfs(v) 

    return bridges

# Graf reprezentowany jako lista sąsiedztwa
#       0 --- 1        3
#       | \   |      / |
#       |  \  |     /  |
#       2 --- 1    4 -- 5
graph1 = [
    [1, 2],      # Sąsiedzi 0
    [0, 2],      # Sąsiedzi 1
    [0, 1],      # Sąsiedzi 2
    [4, 5],      # Sąsiedzi 3
    [3, 5],      # Sąsiedzi 4
    [3, 4]       # Sąsiedzi 5
] # Komponenty: {0,1,2}, {3,4,5}. Brak mostów.
graph2 = [
    [1, 2],      # 0
    [0, 3],      # 1
    [0, 3],      # 2
    [1, 2, 4],   # 3
    [3, 5],      # 4
    [4]          # 5
] # Krawędzie (3,4) i (4,5) są mostami.



print(find_bridges(graph))
