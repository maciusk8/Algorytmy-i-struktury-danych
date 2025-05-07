class Node:
    def __init__(self, value):
        self.value = value
        self.rank = 0
        self.parent = self

G = [ [(1,3), (2,1), (4,2)], # 0
[(0,3), (2,5) ], # 1
[(1,5), (0,1), (3,6)], # 2
[(2,6), (4,4) ], # 3
[(3,4), (0,2) ] ] # 4

def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y: 
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def edgyfi(graph):
    E = []
    for v in range(len(graph)):
        for u, w in graph[v]:
            edge = [v, u, w]
            if edge not in E:
                E.append(edge)
    return E

def MST(graph):
    E = edgyfi(graph)
    E.sort(key=lambda x: x[2])
    MST = []
    V = []
    for i in range(len(graph)):
        V.append(Node(i))
    for i in range(len(E)):
        v = E[i][0]
        u = E[i][1]
        if find(V[v]) != find(V[u]):
            MST.append(E[i])
            union(V[v], V[u])
    return MST

print(MST(G))

    