# Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to miasta a krawędzie to drogi
# łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach jako liczba naturalna).
# Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V, zamieniając się za kierownicą
# w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje, kto prowadzi pierwszy. Proszę zapropnować
# algorytm, który wskazuje taką trasę (oraz osobę, która ma prowadzić pierwsza), żeby Alicja przejechała
# jak najmniej kilometrów.
from queue import PriorityQueue 

def shortest_path(s, t):
    n =len(graph)
    parent = [[None]*2 for i in range(n)] #0-bob 1-alicja
    cost = [[float('inf')]*2 for i in range(n)]



graph = [[(1, 4), (2, 1), (3, 5)],
         [(0, 1), (4, 2)],
         [(0, 1), (5, 8), (6, 7)],
         [(0, 5), (5, 7)],
         [(1, 2), (7, 10)],
         [(2, 8), (3, 7), (8, 3)],
         [(2, 7), (7, 6)],
         [(4, 10), (6, 6), (9, 11)],
         [(5, 3), (9, 9)],
         [(7, 11), (8, 9)]]

start = 0
finish = len(graph) - 1
print(shortest_path(start, finish))