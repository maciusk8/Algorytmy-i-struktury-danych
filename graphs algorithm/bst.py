class Node:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14, Node(13), None)))

def search(node, key):
    while node != None and key != node.val:
        if node.val > key:
            node = node.left
        else:
            node = node.right
    return node

def parent(target, root):
    node = root
    if root == target:
        return None
    parent = root
    while node != None and target != node:
        if node.val > target.val:
            parent = node
            node = node.left
        else:
            parent = node
            node = node.right
    return parent

def succesor(node, root):  #find succesor inorder
    if node.right != None:
        node = node.right
        while node.left != None:
            node = node.left
        return node
    else:
        tmp = parent(node, root)
        while(tmp != None and tmp.left != node):
            tmp = parent(tmp, root)
        return tmp

print(succesor(search(root,8), root))