class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if max(nums) - min(nums) <= 2*k:
            return 0
        else:
            return (max(nums)- k) - (min(nums)+k)