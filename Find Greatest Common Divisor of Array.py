class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = max(nums)
        b = min(nums)
        def helper(a,b):
            if b == 0:
                return a
            return helper(b, a%b)
        return helper(a,b)
