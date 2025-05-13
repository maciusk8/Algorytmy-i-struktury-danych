from egzP9btesty import runtests


def dyrektor(G, R):
	def avaliable_roads(G, R):
		for i in range(len(G)):
			for v in R[i]:
				G[i].remove(v)
		return G
	
	roads = avaliable_roads(G, R)

	return find_eulerian_cycle_directed(roads)

def find_eulerian_cycle_directed(adj):
    stack = []
    cycle = []
    v = 0  # Można zacząć od dowolnego wierzchołka
    stack.append(v)
    
    while stack:
        v = stack[-1]
        if adj[v]:  # Jeśli są jeszcze krawędzie wychodzące
            u = adj[v].pop()  # Usuwamy krawędz
            stack.append(u)
        else:
            cycle.append(stack.pop())
    
    return cycle[::-1]  # Odwracamy kolejność, aby uzyskać poprawny cykl
	
runtests(dyrektor, all_tests=True)
