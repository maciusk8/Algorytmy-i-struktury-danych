from kol2testy import runtests
from collections import deque

def beautree(G):
    def edgyfi(graph):
        edges = []
        for u in range(len(G)):
            for (v, w) in G[u]:
                if u < v:
                    edges.append([u, v,  w])
        return edges

    def to_adj(E, n):
        adj = [[] for _ in range(n)]
        for u, v, w in E:
            adj[u].append(v)
            adj[v].append(u)
        return adj

    def is_connected(BT, n):
        adj = to_adj(BT, n)
        visited = [False]*n
        q = deque()
        q.appendleft(0)
        while q:
            v = q.pop()
            visited[v] = True
            for u in adj[v]:
                if not visited[u]:
                    q.appendleft(u)
        if not all(visited):
            return False
        return True
    
    E = edgyfi(G)
    E.sort(key=lambda x: x[2]) 

    for i in range(len(E) - (len(G) -1) +1):
        BT = E[i:i+len(G)-1]
        if is_connected(BT, len(G)):
            return sum(x[2] for x in BT)        
    
    return None


runtests(beautree, all_tests = True )
