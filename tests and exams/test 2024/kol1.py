from kol1testy import runtests
def maxrank(T):
    maks = 0

    def mergesort(T):
        nonlocal maks
        if len(T) == 1:
            return T
        mid = len(T) // 2
        L = mergesort(T[:mid])
        R = mergesort(T[mid:])
        return merge(L, R)

    def merge(L, R):
        i = j = 0
        c = 0
        m = []
        while i < len(L) and j < len(R):
            if L[i][0] < R[j][0]:
                m.append(L[i])
                c += 1
                i += 1
            else:
                m.append((update(R,j,c)))
                j += 1
        while j < len(R):
            m.append(update(R, j, c))
            j += 1     
        m.extend(L[i:])  
        return m   

    def update(R, j, c):
        nonlocal maks
        num, val = R[j]
        new_rank = val + c
        maks = max(maks, new_rank)
        return num, new_rank
    
    mergesort([(i, 0) for i in T])
    return maks

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True)