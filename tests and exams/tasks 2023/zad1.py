from zad1testy import Node, runtests

class Node:
    def __init__(self):
            self.next = None
            self.val = None

def insert_sort(p, k):
      dummy = Node()
      dummy.next = p 
      prev, curr = p, p.next
      i=0
      while curr != None:
            i+=1
            if prev.val < curr.val:
                prev, curr = curr, curr.next
                continue
            if i <= k:
                 start = dummy
            else:
                 start = start.next
            tmp = start
            while curr.val > tmp.next.val:
                 tmp = tmp.next
            prev.next = curr.next
            curr.next = tmp.next
            tmp.next = curr
            curr = prev.next  
      return dummy.next

def SortH(p,k):
    return insert_sort(p,k)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
