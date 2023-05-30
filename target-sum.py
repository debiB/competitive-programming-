class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ways = 0
        cache = defaultdict(list)
        def dp(pos, _sum):
            nonlocal ways
            if pos >= len(nums):
                return target == _sum
            if (pos, _sum) not in cache:
                cache[(pos,_sum)] = dp(pos + 1, _sum + nums[pos]) + dp(pos + 1, _sum - nums[pos])
            return cache[(pos, _sum)]
        return dp(0, 0)