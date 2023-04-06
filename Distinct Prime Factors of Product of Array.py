class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        ans = set()
        for i in range(len(nums)):
            a=2 
            while(a*a <= nums[i]):
                while(nums[i]%a == 0):
                    nums[i]//=a
                    ans.add(a)
                a+=1
            if nums[i] > 1:
                ans.add(nums[i])
        return len(ans)


    

