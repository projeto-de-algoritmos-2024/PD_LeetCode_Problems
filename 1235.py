from bisect import bisect_right
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Combine startTime, endTime, e profit em uma lista "jobs" ordenados pelo horário de término
        trabalhos = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        
        # Extraímos os horários de término para facilitar uma busca posteriormente
        endTimes = [job[1] for job in trabalhos]
        
        # Inicializamos o vetor que aplicaremos a programação dinâmica, não faremos recursivo, e sim iterativo 
        vetor_PD = [0] * (len(trabalhos) + 1)
        
        # Passaremos por todos os trabalhos
        for i in range(1, len(trabalhos) + 1):
            # Encontraremos o último trabalho compatível, nossa função "p(i)"
            start = trabalhos[i-1][0]

            # Encontramos o maior índice j tal que endTime[j] <= startTime[i]
            ultimo_sem_conflito = bisect_right(endTimes, start) - 1 # 
            
            # Calculando o lucro se "Levar"
            # Se pegarmos esse trabalho, o lucro será o lucro do trabalho atual + lucro acumulado do último trabalho compatível.
            Levar = trabalhos[i-1][2] + (vetor_PD[ultimo_sem_conflito + 1] if ultimo_sem_conflito != -1 else 0)
            
            # Calculando o lucro de "Não Levar"
            # Se não pegarmos o trabalho atual, o lucro será o mesmo do caso anterior.
            Nao_Levar = vetor_PD[i-1]
            
            # Escolhendo o maior entre eles
            vetor_PD[i] = max(Levar, Nao_Levar)
        
        # O último valor do vetor contém o lucro máximo possível escolhendo os trabalhos compatíveis
        return vetor_PD[-1]


# Exemplo de uso
solution = Solution()

# Exemplo 1
startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]
print(solution.jobScheduling(startTime, endTime, profit))  # Output: 120

# Exemplo 2
startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]
print(solution.jobScheduling(startTime, endTime, profit))  # Output: 150

# Exemplo 3
startTime = [1,1,1]
endTime = [2,3,4]
profit = [5,6,4]
print(solution.jobScheduling(startTime, endTime, profit))  # Output: 6
