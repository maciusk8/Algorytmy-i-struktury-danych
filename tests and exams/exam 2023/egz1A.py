from egz1Atesty import runtests
from queue import PriorityQueue

# def gold(G,V,s,t,r):
#   from queue import PriorityQueue

# def gold(G, V, s, t, r):
#     n = len(G)
#     INF = float('inf')
    
#     # cost[v][0] = koszt dotarcia do v bez rabunku
#     # cost[v][1] = koszt dotarcia do v po rabunku
#     cost = [[INF] * 2 for _ in range(n)]
#     cost[s][0] = 0

#     pq = PriorityQueue()
#     pq.put((0, s, 0))  # (koszt, wierzchołek, czy_rabowano)

#     while not pq.empty():
#         c, u, robbed = pq.get()

#         if c > cost[u][robbed]:
#             continue

#         for v, w in G[u]:
#             travel_cost = w * (2 if robbed else 1) + (r if robbed else 0)
#             new_cost = c + travel_cost
#             if new_cost < cost[v][robbed]:
#                 cost[v][robbed] = new_cost
#                 pq.put((new_cost, v, robbed))

#         # Możliwość rabunku, tylko jeśli jeszcze nie było
#         if robbed == 0:
#             rob_gain = V[u]
#             new_cost = c - rob_gain
#             if new_cost < cost[u][1]:
#                 cost[u][1] = new_cost
#                 pq.put((new_cost, u, 1))

#     return min(cost[t][0], cost[t][1])


def gold(G,V,s,t,r):
  n = len(G)
  ds = dijkstra(G, s)
  dt = dijkstra(voilate(G,r), t)
  min_cost = float('inf')
  for v in range(n):
    min_cost = min(min_cost, (ds[v] - V[v] + dt[v]))
  return min_cost

def voilate(G, r):
  n = len(G)
  bad_G = [[] for i in range(n)]
  for v in range(n):
    for u, w in G[v]:
      bad_G[v].append((u, 2*w + r))
  return bad_G

def dijkstra(G,s):
  n = len(G)
  d = [float('inf')]*n
  visited = [False]*n
  d[s] = 0
  q = PriorityQueue()
  q.put((0, s))
  while not q.empty():
    c, v = q.get()
    for u, w in G[v]:
      if not visited[u]:
        if d[u] > d[v] + w:
          d[u] = d[v] + w
          q.put((d[u], u))
    visited[v] = True
  return d

runtests( gold, all_tests = True )
