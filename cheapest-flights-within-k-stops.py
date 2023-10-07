class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [[inf] * n for i in range(n)]
        dp[0][src] = 0
        graph = [[] for i in range(n)]
        for x,y,w in flights:
            graph[x].append([y,w])
        d = k
        for i in range(n - 1):
            for j in range(n):
                if dp[i][j] != inf:
                    for k,w in graph[j]:
                        dp[i + 1][k] = min(dp[i + 1][k],dp[i][j] + w)
        
        ans = inf
        for i in range(min(d + 2,n)):
            ans = min(ans,dp[i][dst])
        return ans if ans != inf else -1