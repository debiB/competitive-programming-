class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ans = []
        prime = [True for _ in range(right+1)]
        prime[0], prime[1] = False, False
        d = 2
        while(d*d <= right):
            if prime[d]:
                i=d*d
                while(i<=right):
                    prime[i] = False
                    i+=d
            d+=1

        for j in range(left, right+1):
            if prime[j]:
                ans.append(j)
        res = [-1,-1]
        min_diff = float("inf")
        for k in range(len(ans)-1):
            diff = ans[k+1] - ans[k]
            if diff < min_diff:
                min_diff= diff
                res = [ans[k], ans[k+1]]
            elif diff == min_diff and res[0] > ans[k]:
                res = [ans[k], ans[k+1]]

        return res
