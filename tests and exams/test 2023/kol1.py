from kol1testy import runtests

def ksum(T, k, p):
    def quickselect(T, s, e, target):
        if s < e:
            pivot = T[e]
            i, j = s-1, s
            while j < e:
                if pivot < T[j]:
                    i+=1
                    T[i], T[j] = T[j], T[i]
                j+=1
            i+=1
            T[i], T[j] = T[j], T[i]
            if i == target:
                return T[i]
            elif i > target:
                return quickselect(T, s, i-1, target)
            else: 
                return quickselect(T, i+1, e, target)
        elif s==e:
            return T[target]
    
    sum = 0
    for i in range(0, len(T)-p+1):
        sum+=quickselect(T[i:i+p], 0, p-1, k-1)
    return sum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
