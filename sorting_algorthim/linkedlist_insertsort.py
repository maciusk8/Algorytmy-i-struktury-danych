class Node:
    def __init__(self, val):
            self.next = None
            self.val = val

def insert_sort(p):
      dummy = Node(-1)
      dummy.next = p 
      prev, curr = p, p.next
      while curr != None:
            if prev.val < curr.val:
                prev, curr = curr, curr.next
                continue
            
            tmp = dummy
            while curr.val > tmp.next.val:
                 tmp = tmp.next
            prev.next = curr.next
            curr.next = tmp.next
            tmp.next = curr
            curr = prev.next  
      return dummy.next


a = Node(2)
b = Node(1)
c = Node(4)
d = Node(3)

a.next = b
b.next = c
c.next = d

start =insert_sort(a)
abs = 0