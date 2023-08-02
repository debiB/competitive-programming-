class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(_sum):
            if _sum == target:
                return 1
            if _sum > target:
                return 0
            ways = 0 
            if _sum not in memo:
                for i in nums:
                    ways += dp(_sum+i)
                memo[_sum]= ways
            return memo[_sum]
        return dp(0)