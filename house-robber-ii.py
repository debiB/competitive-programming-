class Solution:
    def rob(self, nums: List[int]) -> int:
    
        def helper(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                rob = max(rob1+n, rob2)
                rob1 = rob2
                rob2 = rob
            return rob2

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))