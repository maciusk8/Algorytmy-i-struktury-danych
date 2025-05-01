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

def bellmanford(G,s):
    n = len(G)
    d = [float('inf')]*n
    d[s] = 0
    for _ in range(n-1):
        for u in range(n):
            for v,wv in G[u]:
                if d[v]>d[u]+wv:
                    d[v]=d[u]+wv
    return d
print(bellmanford(graph, 1))