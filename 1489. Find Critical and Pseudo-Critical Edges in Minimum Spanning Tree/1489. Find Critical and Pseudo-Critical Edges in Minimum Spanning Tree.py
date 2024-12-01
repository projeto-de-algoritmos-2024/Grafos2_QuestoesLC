from typing import List
import heapq

class Solucao:
    def encontrarArestasCriticas(self, n_nos: int, arestas: List[List[int]]) -> List[int]:
        for indice, aresta in enumerate(arestas):
            aresta.append(indice)
        
        grafo = {i: [] for i in range(n_nos)}
        for inicio, fim, peso, indice in arestas:
            grafo[inicio].append((peso, fim, indice))
            grafo[fim].append((peso, inicio, indice))
        
        def prim(excluir_aresta: int = -1) -> int:
            visitado = [False] * n_nos
            custo_mst = 0
            arestas_usadas = 0
            heap = []
            
            visitado[0] = True
            for peso, vizinho, indice_aresta in grafo[0]:
                if indice_aresta != excluir_aresta:
                    heapq.heappush(heap, (peso, vizinho, indice_aresta))
            
            while heap and arestas_usadas < n_nos - 1:
                peso, no, indice_aresta = heapq.heappop(heap)
                if visitado[no]:
                    continue
                visitado[no] = True
                custo_mst += peso
                arestas_usadas += 1
                for prox_peso, vizinho, indice in grafo[no]:
                    if not visitado[vizinho] and indice != excluir_aresta:
                        heapq.heappush(heap, (prox_peso, vizinho, indice))
            
            return custo_mst if arestas_usadas == n_nos - 1 else float('inf')

        custo_mst_original = prim()

        arestas_criticas = []

        for indice, (inicio, fim, peso, indice_original) in enumerate(arestas):
            if prim(excluir_aresta=indice_original) > custo_mst_original:
                arestas_criticas.append(indice_original)
        
        return arestas_criticas

# Exemplo de uso
solucao = Solucao()
n_nos = 5
arestas = [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]

arestas_criticas = solucao.encontrarArestasCriticas(n_nos, arestas)
print( arestas_criticas)