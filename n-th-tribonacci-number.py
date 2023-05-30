class Solution:
    def tribonacci(self, n: int) -> int:
        d = defaultdict(int)
        d[0] = 0
        d[1] = 1
        d[2] = 1
        def tri(n):
            if n not in d:
                d[n] = tri(n-1) + tri(n - 2) + tri(n-3)
            return d[n]
        return tri(n)