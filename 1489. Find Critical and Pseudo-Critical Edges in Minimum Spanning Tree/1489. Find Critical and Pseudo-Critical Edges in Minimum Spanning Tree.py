from typing import List
import heapq

class Solucao:
    def prim(self, n_nos: int, arestas: List[List[int]]) -> int:
        for indice, aresta in enumerate(arestas):
            aresta.append(indice)
        
        grafo = {i: [] for i in range(n_nos)}
        for inicio, fim, peso, indice in arestas:
            grafo[inicio].append((peso, fim, indice))
            grafo[fim].append((peso, inicio, indice))
        
        visitado = [False] * n_nos
        custo_mst = 0
        arestas_usadas = 0
        heap = []

        visitado[0] = True
        for peso, vizinho, ind_aresta in grafo[0]:
            heapq.heappush(heap, (peso, vizinho, ind_aresta))

        while heap and arestas_usadas < n_nos - 1:
            peso, no, indice = heapq.heappop(heap)
            if visitado[no]:
                continue
            visitado[no] = True
            custo_mst += peso
            arestas_usadas += 1
            for prox_peso, vizinho, ind_aresta in grafo[no]:
                if not visitado[vizinho]:
                    heapq.heappush(heap, (prox_peso, vizinho, ind_aresta))

        return custo_mst if arestas_usadas == n_nos - 1 else float('inf')

solucao = Solucao()
n_nos = 5
arestas = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
custo_mst = solucao.prim(n_nos, arestas)
print("custo da MST:", custo_mst)

