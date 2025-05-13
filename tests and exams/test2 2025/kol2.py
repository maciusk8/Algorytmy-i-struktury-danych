#Maciej Mikołajek
#Mój algorytm to dijkstra powtarzana R-razy ktora zatrzymuje sie gdy osiagnie dowolny resort zwraca
#podowjony koszt oraz numer resortu nastepnie ustawia ten resort jako odwiedzony wiec kolejna
#instancja dijkstry juz do niej nie wejdzie szacowany czas to O(RElogV)

from kol2testy import runtests
from queue import PriorityQueue

def to_adjlist(E): #funkcja ktora przerabia liste krawedzi na liste sasiedztwa
    max_v = -1
    for u, v, w in E:
        max_v = max(u, v, max_v)
    n = max_v + 1
    G = [[] for i in range(n)]
    for u, v , w in E:
        G[v].append((u, w))
        G[u].append((v, w))
    return G 

def lets_roll(start_city, flights, resorts):
    G = to_adjlist(flights) #inicjalizacja listy sasiedztwa
    visited_resorts = [False]*len(G) #tablica informujaca ktory resort jest odwiedzony
    turn = 0
    total_cost = 0
    while turn < len(resorts):
        result = dijkstra(G, start_city, visited_resorts, resorts) #algortytm zwraca [] gdy nie uda sie znalesc juz resortu oraz [koszt, resort] gdy sie uda
        if result:
            cost = result[0]  #tu sie dzieje to co opisalem na samej górze
            r = result[1]
            total_cost+=cost
            visited_resorts[r] = True
        else:
            return total_cost
    return total_cost

def dijkstra(G, s, visited_resorts, resorts): 
    n = len(G)
    visited = [False]*n
    d = [float('inf')]*n 
    q = PriorityQueue()
    q.put((0, s)) #koszt, wierzchołek
    while not q.empty():
        c, v = q.get()
        id = 0
        for resort in resorts:
            if v == resort and not visited_resorts[resort]: #jeśli v to resort zatrzymaj dijkstre i zwroc dane
                return [c*2, resorts.pop(id)] #w celu optymalizacji usuwam resort z resorts ale to chyba nic nie daje i tak :(
            id+=1 
        for u, w in G[v]:
            if not visited[v] and not visited_resorts[v]: 
                if d[u] > c + w:
                    d[u] = c + w
                    q.put((c+w, u))
        visited[v] = True 
    return [] #jesli nie udalo sie znalesc resortu to zwroc pusta liste


runtests(lets_roll, all_tests = True)
