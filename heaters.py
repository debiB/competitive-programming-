class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        ans = []
        def check(num):
            ans = float("inf")
            i,j = 0, len(heaters)-1
            while i <= j:
                mid = (i+j)//2
                if heaters[mid] == num:
                    return 0
                elif heaters[mid] > num:
                    ans = min(ans, abs(heaters[mid] - num))
                    j = mid-1
                elif heaters[mid] < num:
                    ans = min(ans, abs(heaters[mid] - num))
                    i= mid+1
            return ans
        for h in houses:
            ans.append(check(h))
        return max(ans)