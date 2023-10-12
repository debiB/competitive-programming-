# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def find_peak():
            i,j = 0, mountain_arr.length() -1
            while i <= j:
                mid = (i+j)//2
                if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                    i = mid+1
                else:
                    j = mid -1
            return i 
        def bs(is_increasing, start_idx, end_idx):
            i,j = start_idx,end_idx
            while i <= j:
                mid = (i+j)//2
                if mountain_arr.get(mid) == target:
                    return mid
                elif mountain_arr.get(mid) < target:
                    if is_increasing:
                        i = mid+1
                    else:
                        j = mid-1
                else:
                    if is_increasing:
                        j = mid-1
                    else:
                        i = mid+1
            return -1
        idx = find_peak()
        print(idx)
        ans = bs(True, 0, idx)
        if ans == -1:
            ans = bs(False, idx+1, mountain_arr.length()-1)
        return ans