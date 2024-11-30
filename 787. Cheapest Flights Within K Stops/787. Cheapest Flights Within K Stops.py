from heapq import heappush, heappop

def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0

    heap = []
    heappush(heap, (0, inicio))  

    while heap:
        distancia_atual, nodo_atual = heappop(heap)

        if distancia_atual > distancias[nodo_atual]:
            continue

        for vizinho, peso in grafo[nodo_atual]:
            distancia = distancia_atual + peso

            if distancia > distancias[vizinho]:  
                distancias[vizinho] = distancia
                heappush(heap, (distancia, vizinho))

    return distancias

grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

distancias = dijkstra(grafo, 'A')
print(distancias)