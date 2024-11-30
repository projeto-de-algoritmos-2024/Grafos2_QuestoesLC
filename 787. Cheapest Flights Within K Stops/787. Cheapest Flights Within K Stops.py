from heapq import heappush, heappop

def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    custos = {nodo: 0 for nodo in grafo}  

    heap = []
    heappush(heap, (0, inicio, 0)) 

    while heap:
        distancia_atual, nodo_atual, custo_atual = heappop(heap)

        if distancia_atual > distancias[nodo_atual]:
            continue

        for vizinho, peso, preco in grafo[nodo_atual]:
            distancia = distancia_atual + peso
            custo = custo_atual + preco

            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                custos[vizinho] = custo
                heappush(heap, (distancia, vizinho, custo))

    return distancias, custos

grafo = {
    'A': [('B', 1, 5), ('C', 4, 10)], 
    'B': [('A', 1, 5), ('C', 2, 3), ('D', 5, 7)],
    'C': [('A', 4, 10), ('B', 2, 3), ('D', 1, 2)],
    'D': [('B', 5, 7), ('C', 1, 2)]
}

distancias, custos = dijkstra(grafo, 'A')

print("distancia:", distancias)
print("custo acumulados:", custos)

preco_total = sum(custos.values())
print("preco total:", preco_total)

