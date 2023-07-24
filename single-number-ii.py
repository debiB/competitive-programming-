class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            count = 0
            for num in nums:
                if (num>>i) & 1:
                    count+= 1
            if count%3 != 0:
                ans += 2**i
        if ans & 1<<31:
            print(ans & 1<<31)
            ans -= (1<<32)
        return ans