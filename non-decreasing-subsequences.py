from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        def backtrack(idx, li, last):
            nonlocal ans
            if idx == len(nums):
                if len(li) >=2:
                    ans.add(tuple(li))
                return
            if nums[idx] >= last:
                li.append(nums[idx])
                backtrack(idx+1, li, nums[idx])
                li.pop()
            backtrack(idx+1, li, last)

        backtrack(0, [], -100)
        return ans