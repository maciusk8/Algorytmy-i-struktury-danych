#dana jest tablica n liczb chcemy znalezc ta ktora bylaby na pozycji k po posortowaniu
#krok 1 podziel dane na sufit n / 5 grup po 5 elemntow w kazdej grupie znajdz mediane
#krok 2 znajdz mediane median oznaczamy ją x (rekurencyjnie)
#krok 3 wtkonujemy operacje partiton z quicksorta wzgledem x
#krok 4 kontnuujemy jak w zwyklym selectcie //zloznosc liniowa

def magic5(A,k):