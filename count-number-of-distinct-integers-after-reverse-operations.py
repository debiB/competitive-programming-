class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        visit = set()
        def helper(num):
            ans = 0
            while num > 0:
                div = num%10
                ans= ans*10 + div
                num //=10
            return ans
       
        for i  in range(len(nums)):
            visit.add(nums[i])
            visit.add(helper(nums[i]))      
        return len(visit)