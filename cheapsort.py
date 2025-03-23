T = [2,8,4,7,5,7,9,6,20]

def heapyfi(T, n, i):
    left = 2*i + 1
    right = 2*i + 2
    swap_i = i 
    if left < n and T[left] > T[swap_i]:
        swap_i = left
    if right < n and T[right] > T[swap_i]:
        swap_i = right
    if swap_i != i:
        T[i], T[swap_i] = T[swap_i], T[i]
        heapyfi(T, n, swap_i)

def bulidheap(T):
    for i in range(len(T)//2 -1, -1,-1):
        heapyfi(T,len(T), i)

def heapsort(T):
    bulidheap(T)
    for i in range(len(T) - 1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapyfi(T, i, 0)          

heapsort(T)
print(T)         