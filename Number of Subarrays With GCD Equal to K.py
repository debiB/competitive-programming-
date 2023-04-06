class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            g = nums[i]
            for j in range(i, len(nums)):
                g = math.gcd(g, nums[j])
                if g == k:
                    ans+=1
                elif g<k:
                    break
        return ans
