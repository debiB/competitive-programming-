class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        set_even = defaultdict(int)
        set_odd = defaultdict(int)

        for i in range(len(nums)):
            if i % 2 == 0:
                set_even[nums[i]]+=1
            else:
                set_odd[nums[i]]+=1

        first_even, second_even = (-1, 0), (-1, 0)
        for key, val in set_even.items():
            if val > first_even[1]:
                first_even, second_even= (key, val), first_even
            elif val > second_even[1]:
                second_even = (key, val)
        first_odd, second_odd = (-1, 0), (-1, 0)
        for key, val in set_odd.items():
            if val > first_odd[1]:
                first_odd, second_odd= (key, val), first_odd
            elif val > second_odd[1]:
                second_odd = (key, val)
        if first_even[0] != first_odd[0]:
            return len(nums) - (first_even[1]+ first_odd[1])
        else:
            return len(nums) - max(first_even[1]+ second_odd[1], first_odd[1] + second_even[1])