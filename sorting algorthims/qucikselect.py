T = [2,8,4,7,5,7,9,6,5]
def quickselect(T, s, e, k):
    pivot = T[e]
    i, j = s-1, s
    while j < e:
        if T[j] < pivot:
            i+=1
            T[i], T[j] = T[j], T[i]
        j+=1
    i+=1
    T[i], T[j] = T[j], T[i]
    if i == k:
       return pivot
    elif i > k:
       return quickselect(T, s, i-1, k)
    else:
       return quickselect(T, i+1, e, k)

print(quickselect(T,0,len(T)-1,2))
