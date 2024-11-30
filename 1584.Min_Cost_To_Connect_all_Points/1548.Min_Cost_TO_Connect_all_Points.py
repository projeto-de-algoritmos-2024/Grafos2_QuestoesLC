import heapq

def custo_min_pts(pontos):
    n = len(pontos)  
    if n <= 1:
        return 0

    def distancia_manhattan(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    #Variáveis para o Prim
    visitado = [False] * n
    fila_prioridade = [(0, 0)]  
    custo_total = 0  # Custo total MST
    arestas_usadas = 0 

    #Primzudo
    while arestas_usadas < n:

        custo, u = heapq.heappop(fila_prioridade)

        # Ignorar no visitado
        if visitado[u]:
            continue

        # Adicionar no na MST
        visitado[u] = True
        custo_total += custo
        arestas_usadas += 1

        for v in range(n):
            if not visitado[v]:
                distancia = distancia_manhattan(pontos[u], pontos[v])
                heapq.heappush(fila_prioridade, (distancia, v))
    
    return custo_total


if __name__ == "__main__":
    print("Digite o número de pontos:")
    n = int(input().strip()) 
    print("Digite as coordenadas dos pontos (formato: x y):")
    pontos = []
    for _ in range(n):
        x, y = map(int, input().strip().split())
        pontos.append([x, y])

    resultado = custo_min_pts(pontos)
    print(f"Custo mínimo para conectar todos os pontos: {resultado}")