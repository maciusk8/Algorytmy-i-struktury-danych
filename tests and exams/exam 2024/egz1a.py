from egz1atesty import runtests
from queue import PriorityQueue

def rowerize(B, n): #funkcja ktora zamienia B na liste ktora w i posiada najlepszy rower w i
    B_new = [()  for i in range(n)]
    id = 1
    for i, p, q in B: 
      if p < q:
        if B_new[i]:
          if p/q < B_new[i][0]:
            B_new[i] = (p/q, B_new[i][1])
        else:
          B_new[i] = (p/q, id)
          id+=1
    return B_new, id

def to_adjlist(E):
    max_vertex = 0
    for edge in E:
        max_vertex = max(max_vertex, edge[0], edge[1])
        n = max_vertex + 1
    graph = [[] for _ in range(n)]
    for edge in E:
      graph[edge[0]].append((edge[1], edge[2]))
      graph[edge[1]].append((edge[0], edge[2]))
    return graph, n  

def armstrong( B, G, s, t):
    graph, n = to_adjlist(G)
    bicycle, b_cnt = rowerize(B, n)
    dist = [[float('inf')]*(b_cnt+1) for i in range(n)] #id-0 to pieszo
    dist[s][0] = 0
    q = PriorityQueue()
    q.put((0, s, 1, 0)) #koszt, wierzcholek, mnoznik (rower), id roweru
    while not q.empty():
      c, v, m, id = q.get()
      if v == t:
        return int(c)
      if dist[v][id] < c:
        continue
      if id == 0 and bicycle[v]:
        q.put((c, v, bicycle[v][0], bicycle[v][1]))
      for u, w in graph[v]:
        w*=m
        if dist[u][id] > c + w:
          dist[u][id] = c + w
          q.put((c+w, u, m, id))
          

    return -1

  # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
