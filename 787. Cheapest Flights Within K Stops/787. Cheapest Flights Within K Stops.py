from heapq import heappush, heappop
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        grafo = {i: [] for i in range(n)}
        for u, v, preco in flights:
            grafo[u].append((v, 1, preco)) 
        
        distancias = {nodo: float('inf') for nodo in range(n)}
        distancias[src] = 0

        heap = []
        heappush(heap, (0, src, 0, -1)) 

        while heap:
            custo_atual, nodo_atual, distancia_atual, paradas = heappop(heap)

            if nodo_atual == dst and paradas <= k:
                return custo_atual

            if paradas >= k:
                continue

            for vizinho, peso, preco in grafo[nodo_atual]:
                distancia = distancia_atual + peso
                custo = custo_atual + preco

                if distancia <= k + 1:  
                    heappush(heap, (custo, vizinho, distancia, paradas + 1))

        return -1

n = 4  
flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100], [0, 2, 500]]  
src = 1  
dst = 3 
k = 1  

sol = Solution()
result = sol.findCheapestPrice(n, flights, src, dst, k)
print(result)
