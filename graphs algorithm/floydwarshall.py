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

def floydmayweather(G):
    n = len(G)
    d = [[float('inf')]*n for _ in range(n)]
    for v1 in range(n):
        d[v1][v1] = 0
    for v in range(n):
        for u, wu in G[v]:
            d[u][v] = wu
    for u in range(n):
        for v1 in range(n):
            for v2 in range(n):
                if d[v1][u] + d[u][v2] < d[v1][v2]:
                    d[v1][v2] = d[v1][u] + d[u][v2]
    return d

def ilustrate(d):
    n = len(d)
    print("Matrix of distances:")
    for i in range(n):
        print(' '.join(str(dist) if dist != float('inf') else '  ' for j, dist in enumerate(d[i])))
ilustrate(floydmayweather(graph))