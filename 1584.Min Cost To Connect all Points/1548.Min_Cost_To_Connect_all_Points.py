class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        def distancia_manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        # Variáveis para o Prim
        visitado = [False] * n
        fila_prioridade = [(0, 0)]  # (custo, ponto)
        custo_total = 0  # Custo total MST
        arestas_usadas = 0

        # Algoritmo de Prim
        while arestas_usadas < n:
            custo, u = heapq.heappop(fila_prioridade)

            # Ignorar se já foi visitado
            if visitado[u]:
                continue

            # Adicionar ponto à MST
            visitado[u] = True
            custo_total += custo
            arestas_usadas += 1

            for v in range(n):
                if not visitado[v]:
                    distancia = distancia_manhattan(points[u], points[v])
                    heapq.heappush(fila_prioridade, (distancia, v))

        return custo_total