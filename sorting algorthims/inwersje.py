
#problem roziwac mozna za pomoca algorytmu merge sort w ktorym zliczamy przypadki kiedy bierzemy 
#element z "lewej" tablicy, poniewaz wtedy zachodzi inwersja, skoro elementy sa posortowane to wiadomo, ze wieksze ktore zostaly w lewej tablicy
#rownniez posiadaja inwersje ze wszystkimi z prawej co nalezy policzyc
#ja robie to tak ze jesli zostana mi elementy z lewej to mnoze je razy te z prawej i dodaje do licznika inwesji 
#dodatkowo jesli przejdziemy do kolejnego elementu z lewej to rowzniez trzeba zaliczyc poprzednie inwersje
#algorytm ma zlozonosc czasowa nlogn a pamieciowa n  
def count_inversions(A):
    inversions = 0
    def merge_sort(A):
        if len(A) == 1:
            return A
        else:
            l = merge_sort(A[:len(A)//2])
            p = merge_sort(A[len(A)//2:])
            return(merge(l,p))
    def merge(A, B):
        nonlocal inversions
        curr_inv = 0
        i, j = (0,0)
        res = []
        while i < len(A) and j < len (B):
            if A[i] > B[j]:
                inversions+=1   #tutaj zachodzi inwersja w merge sorcie ktora nalezy policzyc
                curr_inv+=1
                res.append(B[j])
                j+=1
            else:
                res.append(A[i])
                i+=1
                if i != len(A): #jesli zostaly nam jakies elementy z lewej i dalej porownojemy to nalezy dodac inwersje ktore juz wystapily poniewaz kolejny element rowniez je posiada 
                    inversions+=curr_inv
        res.extend(B[j:])
        res.extend(A[i:])
        if i != len(A):
            inversions += len(B)*(len(A)-i-1) #finalnie gdy przeszlismy po wszystkich to luksusowo jesli zostaly nam elementy z lewej to mnozymy je razy ilosc elementow z prawej poniewaz zachodza wtedy inwersje. poniewaz wszytkie elementy z prawej strony sa juz mniejsze od mniejszego elementu z lewej
        return res 
    merge_sort(A)
    return inversions
