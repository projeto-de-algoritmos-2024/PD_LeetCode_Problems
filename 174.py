from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[m][n - 1] = dp[m - 1][n] = 1  # Definição da borda da DP

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                min_health = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = max(1, min_health)

        return dp[0][0]

# Testando os casos informados
solution = Solution()

# Caso 1:
dungeon1 = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
print(solution.calculateMinimumHP(dungeon1))  # Output esperado: 7

# Caso 2:
dungeon2 = [[0]]
print(solution.calculateMinimumHP(dungeon2))  # Output esperado: 1