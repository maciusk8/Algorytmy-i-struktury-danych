from kol1testy import runtests
#Moje rozwiazanie bazuje na algorytmie bucket sort, korzystam z faktu, ze paliki które wylądują w wiaderku o długości D nie mogą tworzyc wjazdu dla kombajnu, nalezy jednak uwzgledic fakt ze paliki z sasiednich waiderek rowniez mogą nie tworzyć wjazdu dlatego przy inkrementowaniu wyniku nalezy sprawdzic jeszcze fakt czy roznica poprzedniego palika (najwiekszy palik poprzedniego wiaderka) z najmniejszym (pierwszy palik w aktualnym) jest >=D do sortowania palikow w wiaderku uzywam algorytmu insert sort poniewaz jezeli dane sa w rozkladzie jednostajnym to zlozonosc tego algoryttmu jest pomijalna i przyjmuje ze dzieje sie w czasie stalym czyli zlozonosc czasowa wynosi (n + m/d) poniewaz przechodze po kazdym elemencie w bucket sorcie a potem po ilosci wiwaderek ktora wynosi m/d. zlozonosc pamieciowa wynosi m/d + 1 poniewaz tyle wiaderek trzymam w pamieci

def insertsort(T):
    if len(T) == 1: #prosty algorytm sortujacy bucket sort przyjmuje ze dzieje sie w czasie stalym ze wzgleedu na mala ilosc elementow
        return T
    for i in range(1,len(T)):
        j = i -1
        key = T[i]
        while key < T[j] and j >= 0:
            T[j+1] = T[j]
            j-=1
        T[j+1] = key

def ogrodzenie(M, D, T):
    n = int(M/D) +1  #tworze przedzialy
    buckets = [[] for i in range(n)]
    for el in T:
        buckets[int(el//D)].append(el) #dodaje elementy na podstawie tego ile razy d sie miesci w danym elemencie
    for bucket in buckets:
        insertsort(bucket) #sortuje kazdy przedzial algorytmem insert sort
    result = 0
    prev = -1
    for bucket in buckets:
        if bucket:
            current = bucket[0] #obecny palik ustawiam na najmniejszy w danym przedziale 
            if prev != -1 and current-prev>=D: #patrze na sytuacje opisana na poczatku w ktorej elemnty z sasiednich wiaderek moga nie tworzyc  przejazdu jesli ich roznica < D
              result+=1
            prev = bucket[-1] #ustawiam wczesnijeszy na najdalej polozony palik w danym przedziale
    return result
        

# print(ogrodzenie(T, 10, 0.9))



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ogrodzenie, all_tests = True )
