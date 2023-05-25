class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a,b = float("inf"), float("inf")
        for i in nums:
            if i > b:
              return True
            elif i > a:
                b = min(i,b)
            else:
                a = i 
        return False