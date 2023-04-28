class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak = arr.index(max(arr))
        if peak == 0 or peak == len(arr) - 1:
            return False
        i= peak - 1 
        j = peak+1
        while i > 0 and j < len(arr):
            if arr[i] >= arr[i+1] or arr[j] >= arr[j-1]:
                return False
            i-=1
            j+=1
        while i >= 0:
            if arr[i] >= arr[i+1]:
                return False
            i-=1
        
        while j < len(arr):
            if arr[j] >= arr[j-1]:
                return False
            j+=1 

        return True