from typing import List

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return arr
        
        dig = len(arr) - 1
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                dig = i
                break
        if dig == len(arr) - 1:
            return arr
        
        maxpos = dig + 1
        for j in range(dig + 2, len(arr)):
            if arr[dig] > arr[j] > arr[maxpos]:
                maxpos = j
        
        arr[dig], arr[maxpos] = arr[maxpos], arr[dig]
        return arr