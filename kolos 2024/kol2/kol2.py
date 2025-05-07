from kol2testy import runtests
from collections import deque

def to_adjlist(E):
  max_vertex = 0
  for edge in E:
      max_vertex = max(max_vertex, edge[0], edge[1])
      n = max_vertex + 1
  graph = [[] for _ in range(n)]
  for edge in E:
    graph[edge[0]].append((edge[1], edge[2]))
    graph[edge[1]].append((edge[0], edge[2]))
  return graph


def warrior( G, s, t):
  graph = to_adjlist(G)
  n = len(graph)
  d = [[float('inf')]*17 for i in range(n)]
  d[s][0] = 0
  q = deque()
  q.appendleft((s, 0, 0, 0)) 
  while q:
      v, p, time, tired = q.pop()
      if v == t:
         return time  
      if p == 0:
        if d[v][tired] < time:
            continue
        for u, w in graph[v]:
            if tired + w <= 16:
              d[u][tired+w] =time + w
              q.appendleft((u, time + w, time + w, tired + w))
            else:
               if d[v][0] > time + 8:
                d[v][0] = time + 8
                q.appendleft((v, time + 8, time+8, 0))
      else:
         q.appendleft((v, p-1, time, tired))
  return -1



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )

#wersja dijkstra   
# from kol2testy import runtests
# from queue import PriorityQueue 

# def to_adjlist(E):
#   max_vertex = 0
#   for edge in E:
#       max_vertex = max(max_vertex, edge[0], edge[1])
#       n = max_vertex + 1
#   graph = [[] for _ in range(n)]
#   for edge in E:
#     graph[edge[0]].append((edge[1], edge[2]))
#     graph[edge[1]].append((edge[0], edge[2]))
#   return graph


def warrior( G, s, t):
  graph = to_adjlist(G)
  n = len(graph)
  d = [[float('inf')]*17 for i in range(n)]
  d[s][0] = 0
  q = PriorityQueue()
  q.put((0, s, 0)) 
  while not q.empty():
      time, v, tired = q.get()
      if v == t:
         return time
      if d[v][tired] < time:
          continue
      if d[v][0] > time + 8:
          d[v][0] = time + 8
          q.put((time+8, v, 0))
      for u, w in graph[v]:
          if tired + w <= 16:
             d[u][tired+w] =time + w
             q.put((time + w, u, tired + w))
  return -1



# # zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( warrior, all_tests = True )
