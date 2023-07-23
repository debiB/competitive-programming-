class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        bit_op = []*((2**len(nums)) - 1)
        def perform_or(arr):
            res = 0
            for i in arr:
               res |= i
            return res 
        def backtracking(idx, list):
            if idx >= len(nums):
                bit_op.append(perform_or(list[:]))
                return
            list.append(nums[idx])
            backtracking(idx+1,list)
            list.pop()
            backtracking(idx+1,list)

        backtracking(0,[])
        return bit_op.count(max(bit_op))