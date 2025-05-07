# Dana jest tabela kursów walut. Dla każdych dwóch walut 'x' oraz 'y' wpis K[x][y] oznacza ile trzeba
# zapłacić waluty 'x' żeby otrzymać jednostkę waluty 'y'. Proszę zaproponować algorytm, który sprawdza
# czy istnieje taka waluta 'z', że za jednostkę 'z' można uzyskać więcej niż jednostkę 'z' przez serię
# wymian walut.
from math import log10

def logaritmize_and_max(currencies):
    n = 0
    for i in range(len(currencies)):
        v, u, w = currencies[i]
        currencies[i] = (v, u, -log10(w))
        n = max(n, u, v)
    return currencies, n+1

def bellman_fordziarz(currencies, z):
    currencies, n = logaritmize_and_max(currencies)
    cost = [float('inf')]*n
    cost[z] = 0
    for i in range(0, n-1):
        for v, u, w in currencies:
            cost[u] = min(cost[u], cost [v] + w)
    return currencies, cost, n

def currency_exchange(currencies, z):
    currencies, cost, n = bellman_fordziarz(currencies, z)
    for v, u, w in currencies:
        if cost[u] < cost[v] + w:
            return True
    return False

currencies = [
    (0, 1, 2.0),     # Z 1 jednostki 0 dostajesz 2 jednostki 1
    (1, 2, 2.0),     # Z 1 jednostki 1 dostajesz 2 jednostki 2
    (2, 0, 0.2)      # Z 1 jednostki 2 dostajesz 0.2 jednostki 0
]

print(currency_exchange(currencies, 0))