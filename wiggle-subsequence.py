class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        max_len, last = 1, None
        for i in range(1,len(nums)):
            diff = nums[i] - nums[i-1]
            if(diff > 0 and last != 1) or (diff < 0 and last != -1):
                max_len+=1
                last = 1 if diff > 0 else -1
        return max_len