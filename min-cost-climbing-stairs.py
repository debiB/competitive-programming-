class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return min(cost)
        d  = [-1]*(len(cost))
        d[0] = cost[0]
        d[1] = cost[1]
        def minC(n):
            if d[n] == -1:
               d[n] = cost[n] + min(minC(n-1), minC(n-2))
            return d[n]
        minC(len(cost)-1)
        return min(d[-2], d[-1])