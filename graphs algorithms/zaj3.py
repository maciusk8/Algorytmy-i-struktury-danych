
"""
1. Algorytm dijkstry,
    rep. macierzowa
2. odtwarzanie/wypisywanie najkrotszej sciezki na podstawie tablicy parentow
3. prosze podac algorytm znajdujacy najkrotsza sciezke w dagu
4. dlugoscia sciezki jest iloczyn jej wag. zaproponowac jak najszybszy/najlepszy algorytm
znajdujacy najkrotsze sciezki
5. przewodnik turystyczny-
mamy graf z miastami startowymi s i t, mamy krawedzie - polaczenia autobusowe, autobusy maja pojemnosc
- ile osob moga przewiezc, sciezka o maksymalnej pojemnosci
chcemy sciezke gdzie minimalna waga jest jak najwieksza
6. graf i dlugosci wyrazone w kilometrach, s, t, stacje benzynowe z paliwem w roznych cenach
samochod pali litr na kilometr , pojemnosc baku d
7.dwoch kierwocow jedziemy z miasta s do miasta t bob chche wybrac takak trase zeby kierowac
jak najmniej potem prowadzi alicja i na samym koncu znowu bob  
8. chcemy znalezvv najkrotsza sciezke przebiegajaca po krawdziach o malejachych wagach  
"""
# 1.umieszczamy w kolcje pioytetowej typu max
# 2.sciagamy krawdz umax vmax
# waga maksymalna jest pamietana