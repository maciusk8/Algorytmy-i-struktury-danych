from typing import (
    List,
    Tuple,
)
from queue import Queue

"""
graf nieskierowany G = (v, e) kazfa krawedz ma inna wage ze zbioru {1...e}
czy istnieje sciezka z s to t po krawedziach o malejacych wagach
"""
#(sasiad, waga)
graph = [
    [(1, 4), (3, 9)],                 #  Wierzchołek 0
    [(0, 4), (2, 6), (4, 2)],          # Wierzchołek 1
    [(1, 6), (3, 8), (5, 5), (6, 3)],  # Wierzchołek 2
    [(0, 9), (2, 8), (5, 7)],          # Wierzchołek 3
    [(1, 2), (5, 1)],                  # Wierzchołek 4
    [(2, 5), (3, 7), (4, 1), (6, 10)], # Wierzchołek 5
    [(2, 3), (5, 10)]                  # Wierzchołek 6
]

e = 20 #liczba krawedzi
s = 0  # start
t = 6  # koniec

Node_t = Tuple[int, int]

def counting_sort(T: List[Node_t]) -> List[Node_t]:
    n = len(T)
    A = [0]*e
    for edge in T:
        A[edge[1]]+=1
    
    for i in range(e-2, -1, -1):
        A[i] = A[i+1] + A[i]

    B = [0]*n
    for i in range(n-1,-1,-1):
        A[T[i][1]]-=1
        B[A[T[i][1]]] = T[i]
    return B

def sortgraph(G):
    n = len(G)
    SG = []
    for i in range(n):
        SG.append(counting_sort(G[i]))
    return SG

def solution(G):
    n = len(G)
    price = [0]*n
    Q = Queue()
    Q.put(s)
    price[s] = e+1
    while not Q.empty():
        v = Q.get()
        print(v)
        for u, w in graph[v]:
            if w > price[v]:
                break
            if price[u] < w and w < price[v]:
                if u == t:
                    return True
                Q.put(u)
                price[u] = w 
    return False

print(solution(sortgraph(graph)))
