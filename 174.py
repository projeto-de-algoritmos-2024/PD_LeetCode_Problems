from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # Criamos uma matriz para o algoritmo da Programação dinâmica
        m, n = len(dungeon), len(dungeon[0])

        # Inicializamos e adicionamos uma linha e coluna extra com infinito, para facilitar o cálculo nas bordas
        matriz = [[float('inf')] * (n + 1) for _ in range(m + 1)]

        # Definimos a borda (canto inferior direito) da matriz com 1, pois o cavaleiro precisa de pelo menos 1 para sair
        matriz[m][n - 1] = matriz[m - 1][n] = 1  

        # Iremos de trás para frente, ou seja, da saída para a origem
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Só pode ir ou para baixo ou para direita, pegaremos o min entre eles e subtraímos o valor da célula da dungeon
                # Se a célula tem um monstro (dungeon[i][j] < 0), precisaremos de mais HP.
                # Se tem um bônus de vida (dungeon[i][j] > 0), precisaremos de menos HP.
                HP_minimo = min(matriz[i + 1][j], matriz[i][j + 1]) - dungeon[i][j]

                # Garantindo que o HP nunca seja menor que 1
                matriz[i][j] = max(1, HP_minimo)

        # A matriz na posição [0][0] terá o HP mínimo para cruzar a dungeon
        return matriz[0][0]

# Testando os casos informados
solution = Solution()

# Caso 1:
dungeon1 = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
print(solution.calculateMinimumHP(dungeon1))  # Output esperado: 7

# Caso 2:
dungeon2 = [[0]]
print(solution.calculateMinimumHP(dungeon2))  # Output esperado: 1