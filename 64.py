from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Inicializando a primeira linha (só pode vir da esquerda)
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        # Inicializando a primeira coluna (só pode vir de cima)
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        # Preenchendo a matriz usando programação dinâmica
        for i in range(1, m):
            for j in range(1, n):
                # Escolhemos o menor custo entre:
                                  # vir de cima # vir da esquerda
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        # Retorna o menor caminho para a última célula
        return grid[-1][-1]  

# Testando os casos informados
sol = Solution()
print(sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))  # Saída esperada: 7
print(sol.minPathSum([[1,2,3],[4,5,6]]))  # Saída esperada: 12