from bisect import bisect_right
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Combine startTime, endTime, and profit into a list of jobs
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        
        # Extract sorted endTimes
        endTimes = [job[1] for job in jobs]
        
        # Initialize dp array
        dp = [0] * (len(jobs) + 1)
        
        for i in range(1, len(jobs) + 1):
            # Find the latest job that doesn't conflict with jobs[i-1]
            start = jobs[i-1][0]
            last_non_conflict = bisect_right(endTimes, start) - 1
            
            # Calculate the profit if we include the current job
            profit_including_current = jobs[i-1][2] + (dp[last_non_conflict + 1] if last_non_conflict != -1 else 0)
            
            # Calculate the profit if we exclude the current job
            profit_excluding_current = dp[i-1]
            
            # Choose the maximum profit
            dp[i] = max(profit_including_current, profit_excluding_current)
        
        return dp[-1]


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
