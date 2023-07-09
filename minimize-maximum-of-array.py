class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        max_mean = nums[0]
        _sum = max_mean
        for i in range(1,len(nums)):
            _sum += nums[i]
            avg = ceil(_sum/(i+1))
            max_mean = max(max_mean, avg)
        return max_mean