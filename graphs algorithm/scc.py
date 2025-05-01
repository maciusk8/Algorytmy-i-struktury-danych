graph = [
    [1, 4],   
    [5],       
    [1, 3, 6], 
    [6],       
    [0, 5],    
    [2, 6],    
    [7],   
    [3]         
]

graph2 = [
    [1],
    [0,2],
    [1]
]

def scc(graph):
    n = len(graph)
    id = 0
    lowlink = [-1]*n
    ids = [-1]*n
    stack = []
    on_stack = [False]*n

    def dfs(v):
        nonlocal lowlink, stack, on_stack, ids, n, id
        ids[v] = id
        lowlink[v] = id
        stack.append(v)
        on_stack[v] = True
        id+=1
        for u in graph[v]:
            if ids[u] == -1:
                dfs(u)
            if on_stack[u]: 
                lowlink[v] = min(lowlink[u], lowlink[v])
        if ids[v] == lowlink[u]:
            while(True):
                node = stack.pop()
                on_stack[node] = False
                # lowlink[node] = ids[v]
                if node == v:
                    break

    for v in range(n):
        if ids[v] == -1:
            dfs(v)
    
    print(lowlink)
    return lowlink  

scc(graph2)