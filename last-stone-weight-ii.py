class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = math.ceil(sum(stones)/2)
        def dfs(i, _sum):
            nonlocal total
            if _sum >= total or i >= len(stones):
               return abs(_sum - (sum(stones) - _sum))
            if (i, _sum) in dp:
                return dp[(i,_sum)]
            dp[(i, _sum)] = min(dfs(i+1,_sum), dfs(i+1, _sum + stones[i]))
            return dp[(i,_sum)]
        dp = {}
        return dfs(0,0)