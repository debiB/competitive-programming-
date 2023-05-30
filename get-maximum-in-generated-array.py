class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        d = defaultdict(int)
        _max = 0
        def get_max(n):
            if n == 0 or n == 1:
                d[n] = n
            if n not in d:
                if n%2 == 1:
                    d[n] = get_max(n//2) + get_max((n//2)+1)
                else:
                    d[n] = get_max(n//2)
            return d[n]

        for i in range(n+1):
            get_max(i)
        for val in d.values():
            _max = max(_max, val)    
        return _max