def insertsort(T):
    if len(T) == 1:
        return T
    for i in range(1,len(T)):
        j = i -1
        key = T[i]
        while key < T[j] and j >= 0:
            T[j+1] = T[j]
            j-=1
        T[j+1] = key

def bucketsort(T):
    n = len(T)
    buckets = [[] for i in range(n)]
    for el in T:
        buckets[int(n*el)].append(el)
    for bucket in buckets:
        insertsort(bucket)
    i=0
    for bucket in buckets:
        for el in bucket:
            T[i] = el
            i+=1
T = [0.1, 0.05, 0.0002, 0.7, 0.3, 0.52, 0.34, 0.0004]
bucketsort(T)
print(T)