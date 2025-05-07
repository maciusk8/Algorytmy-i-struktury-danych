def articulation_points(G):
    n = len(G)
    d = [-1]*n
    low = [-1]*n
    time  = 0 
    a_points = []
    def dfs(v, p=-1):
        nonlocal d, low, time, a_points
        low[v] = d[v] = time 
        time+=1
        for u in G[v]:
            if u == p:
                continue
            else:
                if id[u] == -1:
                    dfs(u, v)
                low[v] = min(low[v], low[u])
                