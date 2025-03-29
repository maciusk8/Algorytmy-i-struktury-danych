# wszystkie liczby dzielimy przez M by byly w zakresie 0-1
# znajdujemy srednia z elementow by wyznaczyc przyblizona pozycje p
# tworzymy n/4 kubelkow z prawej strony p i n/4 kubelkow z lewej strony p
# uzywamy bucket sort by posortowac elementy
# przechodzimy po posortowanej tablicy i znajdujemy wjazdy
# wszystkie operacje liniowe wiec zlozonosc liniowa o(n)
# jeden test nie przechodzi prawdopodobnie przez niedokladnosc liczb zmiennoprzecinkowych

from kol1testy import runtests

def srednia(T):
  n = len(T)
  sum = 0
  for x in T:
    sum += x
  return sum / n

def normalize(T, M):
  for i in range(0, len(T)):
    T[i] /= M

def find_place(x, l, r, n):
  size = r - l
  return int(((x - l) / size) * n)

def insert_sort(T):
  n = len(T)
  if n == 0:
    return
  res = [T[0]]
  for i in range(1, n):
    j = 0
    flag = False
    while j < len(res):
      if T[i] < res[j]:
        flag = True
        res.insert(j, T[i])
        break
      j += 1
    if not flag:
      res.append(T[i])
  return res

def bucket_sort(T, p, M):
  n = len(T)
  p = srednia(T)
  
  B = list()
  for i in range(0, n//2):
    B.append(list())
  for i in range(0, n):
    if T[i] < p:
      place = find_place(T[i], 0, p, n//4)
    else:
      place = find_place(T[i], p, 1.0, n//4) + n//4
    B[place].append(T[i])
  for i in range(0, n//2):
    B[i] = insert_sort(B[i])
  Tso = list()
  for tab in B:
    if tab != None:
      for x in tab:
        Tso.append(x)
  return Tso

  
  

def ogrodzenie(M, D, T):
  D /= M
  normalize(T, M)
  p = srednia(T)
  Tso = bucket_sort(T, p, M)
  prev = Tso[1]
  count = 0
  for i in range(1, len(Tso)):
    if Tso[i] - prev >= D:
      count += 1
    prev = Tso[i]
  return count


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ogrodzenie, all_tests = True )
