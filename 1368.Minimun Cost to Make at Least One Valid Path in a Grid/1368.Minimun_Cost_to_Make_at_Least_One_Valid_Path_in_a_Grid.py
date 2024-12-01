import heapq
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        direções = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
        # (custo, linha, coluna)
        heap = [(0, 0, 0)]  
        # Matriz custo minimo 
        custo_minimo = [[float('inf')] * n for _ in range(m)]
        custo_minimo[0][0] = 0

        while heap:
            custo, x, y = heapq.heappop(heap)

            if x == m - 1 and y == n - 1:
                return custo

            if custo > custo_minimo[x][y]:
                continue

            for i, (dx, dy) in enumerate(direções):
                nx, ny = x + dx, y + dy 

                 # verifica se esta na matriz 
                if 0 <= nx < m and 0 <= ny < n: 
                  
                    novo_custo = custo + (1 if grid[x][y] != i + 1 else 0)
                    if novo_custo < custo_minimo[nx][ny]:
                        custo_minimo[nx][ny] = novo_custo
                        heapq.heappush(heap, (novo_custo, nx, ny))

        return -1