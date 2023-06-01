class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d = defaultdict(int)

        def dp(target):
            if target < 0:
                return float("inf")
            if target == 0:
                return 0
            if target not in d:
                d[target] = float("inf")
                for i in coins:
                    d[target] = min(d[target],dp(target-i) +1)
            return d[target]   
        return  dp(amount) if  dp(amount) != float("inf") else -1