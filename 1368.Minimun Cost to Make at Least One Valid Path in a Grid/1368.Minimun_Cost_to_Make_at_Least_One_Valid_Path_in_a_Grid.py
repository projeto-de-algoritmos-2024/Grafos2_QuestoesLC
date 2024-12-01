import heapq

class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])

        # Direções de movimentação
        direções = [(0, 1), (0, -1), (1, 0), (-1, 0)] 

        heap = [(0, 0, 0)]  # (custo, x, y)

        custo_minimo = [[float('inf')] * n for _ in range(m)]
        custo_minimo[0][0] = 0  

        passos = []  

        def print_custo_minimo():  
            print("Matriz custo minimo:")
            for linha in custo_minimo:
                print(linha)
            print()

        while heap:
            custo, x, y = heapq.heappop(heap)  
            passos.append(f"Desenfileira: custo={custo}, x={x}, y={y}")

            if custo > custo_minimo[x][y]:
                passos.append(f"Ignorado: custo={custo} > custo_minimo={custo_minimo[x][y]}")
                continue

            for i, (dx, dy) in enumerate(direções):
                nx, ny = x + dx, y + dy

                novo_custo = custo + (1 if grid[x][y] != i + 1 else 0)

                if novo_custo < custo_minimo[nx][ny]:  
                    custo_minimo[nx][ny] = novo_custo
                    heapq.heappush(heap, (novo_custo, nx, ny))
                    passos.append(f"enfileira: custo={novo_custo}, x={nx}, y={ny}")
                    print_custo_minimo()  

        
        for passo in passos:
            print(passo)

        return custo_minimo

if __name__ == "__main__":
    solution = Solution()
    grid = [[1, 1, 3], [3, 2, 2], [1, 1, 4]]
    solution.minCost(grid)