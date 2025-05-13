from egz3atesty import runtests
from collections import deque

def mykoryza( G,T,d ):
    n = len(G)
    time = [float('inf')]*n
    shroom_id = [-1]*n
    q = deque()
    for i, start in enumerate(T):
        shroom_id[start] = i
        time[start] = 0
        q.append((start, 0))
    while q:
        v, t = q.popleft()
        for u in G[v]:
            if time[u] > t + 1:
                shroom_id[u] = shroom_id[v] 
                time[u] = t + 1
                q.append((u, t+1))
            elif time[u] == t + 1 and shroom_id[u] > shroom_id[v]:
                shroom_id[u] =  shroom_id[v]
    return sum(1 for source in shroom_id if source == d)

  

runtests( mykoryza, all_tests = True )
