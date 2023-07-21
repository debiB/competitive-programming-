class Solution:
    def isPossible(self, nums):
        freq_map = {}
        end_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        for num in nums:
            if freq_map[num] == 0:
                continue

            freq_map[num] -= 1

            if end_map.get(num - 1, 0) > 0:
                end_map[num - 1] -= 1
                end_map[num] = end_map.get(num, 0) + 1
            elif freq_map.get(num + 1, 0) > 0 and freq_map.get(num + 2, 0) > 0:
                freq_map[num + 1] -= 1
                freq_map[num + 2] -= 1
                end_map[num + 2] = end_map.get(num + 2, 0) + 1
            else:
                return False

        return True