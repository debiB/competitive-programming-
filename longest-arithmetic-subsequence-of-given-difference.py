class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = {}
        ans = 0
        for num in arr:
            if num - difference in memo:
                memo[num] = memo[num - difference] + 1
            else:
                memo[num] = 1
            ans = max(ans, memo[num])
        return ans