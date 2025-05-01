'''
Problem: Najtańsza podróż samochodem z ograniczeniami paliwowymi

Opis:
Jesteś kierowcą samochodu podróżującego po sieci miast/punktów.
Sieć miast reprezentowana jest jako graf, gdzie wierzchołki to miasta,
a krawędzie to drogi o określonych długościach w kilometrach.
Samochód ma ograniczoną pojemność baku i zużywa paliwo w tempie 1 litr na 1 km.
Na niektórych wierzchołkach (miastach) znajdują się stacje benzynowe,
gdzie można zatankować paliwo po podanej cenie za litr (ceny mogą się różnić
między stacjami). Celem jest znalezienie minimalnego kosztu pieniężnego
podróży z wierzchołka startowego do wierzchołka docelowego.

Zakładamy, że:
- Zużycie paliwa wynosi dokładnie 1 litr na 1 km.
- Odległości między miastami są podane w kilometrach (liczby całkowite).
- Pojemność baku jest stała.
- Można tankować dowolną ilość paliwa aż do pełnego baku (w ramach dostępnych funduszy).
- Graf może być nieskierowany (jeśli można przejechać z A do B, to i z B do A).

Dane wejściowe:
- Graf w postaci listy sąsiedztwa: `lista_sasiedztwa[u]` to lista krotek `(v, odległość_uv)`,
  gdzie `v` to sąsiad wierzchołka `u`, a `odległość_uv` to długość krawędzi.
- `pojemnosc_baku`: Maksymalna pojemność baku samochodu w litrach.
- `start_node`: Indeks wierzchołka startowego.
- `target_node`: Indeks wierzchołka docelowego.
- `poczatkowe_paliwo`: Poziom paliwa w baku na starcie podróży.
- `ceny_paliwa`: Lista, gdzie `ceny_paliwa[u]` to cena 1 litra paliwa
  na stacji w wierzchołku `u`. Wartość `-1` oznacza brak stacji w danym wierzchołku.

Wynik:
Minimalny łączny koszt pieniężny poniesiony na zakup paliwa podczas podróży
z `start_node` do `target_node`. Jeśli podróż jest niemożliwa, wynikiem może być
nieskończoność lub odpowiedni wskaźnik.

Metoda rozwiązania (sugerowana):
Konstrukcja rozszerzonego grafu stanów (wierzchołki to pary `(wierzchołek_grafu, poziom_paliwa)`)
i zastosowanie algorytmu Dijkstry na tym grafie w celu znalezienia ścieżki
o minimalnym koszcie (sumie cen paliwa).
'''

pojemnosc_baku = 5
start_node = 0
target_node = 3

lista_sasiedztwa = [
    [(1, 2), (3, 5)],
    [(2, 2)],
    [(3, 2)],
    [(0, 5)]
]

ceny_paliwa = [
    10,
    3,
    3,
    2,
]

def solve():
    

