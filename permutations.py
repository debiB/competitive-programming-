class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(list, bitmask):
            nonlocal res
            if len(list) == len(nums):
                res.append(list.copy())
                return 
            
            for i in  range(len(nums)):
                if bitmask & (1<< i) == 0:
                    bitmask |= (1<< i)
                    list.append(nums[i])
                    backtrack(list, bitmask)
                    bitmask &= ~(1<< i)
                    list.pop()
        backtrack([],0)
        return res