from heapq import heappush, heappop
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        grafo = {i: [] for i in range(n)}
        for u, v, preco in flights:
            grafo[u].append((v, preco))  

        distancias = [[float('inf')] * (k + 2) for _ in range(n)]
        distancias[src][0] = 0  

        heap = []
        heappush(heap, (0, src, 0)) 

        while heap:
            custo_atual, nodo_atual, paradas = heappop(heap)

            if paradas > k:
                continue

            if custo_atual > distancias[nodo_atual][paradas]:
                continue

            for vizinho, preco in grafo[nodo_atual]:
                novo_custo = custo_atual + preco
               
                if novo_custo < distancias[vizinho][paradas + 1]:
                    distancias[vizinho][paradas + 1] = novo_custo
                    heappush(heap, (novo_custo, vizinho, paradas + 1))

        resultado = min(distancias[dst][:k + 2])

        return resultado if resultado != float('inf') else -1

