T = [2,8,4,7,5,7,9,6,5]

def quicksort(T, s, e):
    if e > s:
        pivot = T[e]
        i, j = s-1, s
        while j < e:
            if T[j] < pivot:
                i+=1
                T[i], T[j] = T[j], T[i]
            j+=1
        i+=1
        T[i], T[j] = T[j], T[i]
        quicksort(T,0,i-1)
        quicksort(T,i+1,e)

    
    
quicksort(T, 0 , len(T)-1)
print(T)