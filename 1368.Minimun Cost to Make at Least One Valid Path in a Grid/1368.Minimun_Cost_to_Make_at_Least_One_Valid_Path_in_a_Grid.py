import heapq

class Solution:
    def minCost(self, grid):

        heap = [(0, 0, 0)]  # (custo, x, y) 
        passos = []  

        while heap:
            custo, x, y = heapq.heappop(heap)  
            passos.append(f"Desenfileirou: custo={custo}, x={x}, y={y}")
            
           
            if x + 1 < len(grid):  
                heapq.heappush(heap, (custo + 1, x + 1, y))
                passos.append(f"Enfileirou: custo={custo + 1}, x={x + 1}, y={y}")
            
            if y + 1 < len(grid[0]):  
                heapq.heappush(heap, (custo + 1, x, y + 1))
                passos.append(f"Enfileirou: custo={custo + 1}, x={x}, y={y + 1}")
            
            if not heap:  
                passos.append("Heap vazia.")
        
        for passo in passos: 
            print(passo)

if __name__ == "__main__":
    solution = Solution()
    grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]] 
    solution.minCost(grid)