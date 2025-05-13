from zad6testy import runtests
from heapq import heappush, heappop
def jumper(G, s, w):
    n = len(G)
    INF = float('inf')
    dist = [[INF] * 3 for _ in range(n)]  # 0 = normal, 1 = po 1. krawędzi skoku, 2 = po skoku
    dist[s][0] = 0
    pq = [(0, s, 0, 0)]  # (dystans, wierzchołek, tryb, koszt_pierwszej_krawędzi_skoku)

    while pq:
        d, u, mode, prev_cost = heappop(pq)
        if dist[u][mode] < d:
            continue

        for v in range(n):
            c = G[u][v]
            if c == 0:
                continue

            if mode == 0:
                # 1. zwykły ruch
                if d + c < dist[v][0]:
                    dist[v][0] = d + c
                    heappush(pq, (d + c, v, 0, 0))
                # 2. rozpoczęcie skoku
                if d + c < dist[v][1]:
                    dist[v][1] = d + c
                    heappush(pq, (d + c, v, 1, c))  # zapamiętaj c1 jako prev_cost

            elif mode == 1:
                # kontynuacja skoku – zakończenie go
                cost = max(prev_cost, c)
                if d - prev_cost + cost < dist[v][2]:
                    dist[v][2] = d - prev_cost + cost
                    heappush(pq, (d - prev_cost + cost, v, 2, 0))

            elif mode == 2:
                # tylko zwykły ruch
                if d + c < dist[v][0]:
                    dist[v][0] = d + c
                    heappush(pq, (d + c, v, 0, 0))

    return min(dist[w])



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )