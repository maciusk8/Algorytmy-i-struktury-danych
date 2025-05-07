# Pewien podróżnik chce przebyć trasę z punktu A do punktu B. Niestety jego samochód spala dokładnie jeden
# litr paliwa na jeden kilometr trasy. W baku mieści się dokładnie D litrów paliwa. Trasa jest reprezentowana
# jako graf, gdzie wierzchołki to miasta a krawędzie to łączące je drogi. Każda krawędź ma długość w
# kilometrach (przedstawioną jako liczba naturalna). W każdym wierzchołku jest stacja benzynowa, z daną ceną
# za litr paliwa. Proszę podać algorytm znajdujący trasę z punktu A do punktu B o najmniejszym koszcie.
from queue import PriorityQueue 

def cheapest_trip_with_refueling(city_a, city_b, capacity):
    n = len(graph)
    d = [[float('inf')]*(capacity+1) for i in range(n)]
    d[city_a][capacity] = 0
    q = PriorityQueue()
    q.put((0, city_a, 0))
    while not q.empty():
        time, v, fuel = q.get()
        if v == city_b:
            return time
        if d[v][fuel] < time:
            continue
        if fuel < capacity:
            new_time = time + costs[v]
            if d[v][fuel + 1] > new_time:
                d[v][fuel +1] = new_time
                q.put((new_time, v, fuel+1))
        for u, w in graph[v]:
            if fuel - w >= 0:
                if d[u][fuel - w] > time:
                  d[u][fuel- w] = time
                  q.put((time, u, fuel-w))
    return -1



graph = [
         [(1, 5), (2, 3)],
         [(0, 4), (2, 3), (3, 5)],
         [(0, 3), (1, 3), (3, 4)],
         [(1, 5), (2, 4), (4, 6)],
         [(3, 6)]
        ]
costs = [
    8,
    5,
    3,
    2,
    1
]

city_a = 0
city_b = len(graph) - 1
print(cheapest_trip_with_refueling(city_a, city_b, 6))