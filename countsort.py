T = [2,8,4,7,5,7,9,6,20]

def countsort(T):
    C = [0]*(max(T)+1)
    for i in range(len(T)):
        C[T[i]]+=1
    for i in range(1, len(C)):
        C[i] = C[i-1] + C[i]
    
    B = [0]*len(T)
    for i in range(len(B)-1, -1, -1):
        C[T[i]] -= 1
        B[C[T[i]]] = T[i]

countsort(T)
print(T)

