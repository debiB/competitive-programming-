import sys, os, io
from collections import defaultdict
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
inf = 5 * 10**16
 
for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    go_to = defaultdict(list)
    coords = set()
    coords.add((1, 1))
    coords.add((n, m))
    for i in range(k):
        p, q, r, s, t = map(int, input().split())
        go_to[p * m + q] += [[r, s, t]]
        coords.add((p, q))
        coords.add((r, s))
    coords = sorted(list(coords))
    N, index = len(coords), {}
    dp, prefix, suffix = [-inf] * N, [-inf] * N, [-inf] * N
    for i in range(N): index[coords[i]] = i
    pairs, i = [], 0
    dp[0] = 0
    while i < N:
        j = i
        while j + 1 < N and coords[j + 1][0] == coords[j][0]:
            j += 1
            if coords[j][0] == 1:
                dp[j] = -a[0] * (coords[j][1] - 1)
        pairs += [(i, j)]
        i = j + 1
    for start, end in pairs:
        leftVal = rightVal = -inf
        for i in range(start, end + 1):
            x, y = coords[i]
            leftVal = max(leftVal, prefix[i])
            dp[i] = max(dp[i], leftVal - a[x - 1] * (y - 1))
        for i in range(end, start - 1, -1):
            x, y = coords[i]
            rightVal = max(rightVal, suffix[i])
            dp[i] = max(dp[i], rightVal - a[x - 1] * (m - y))
        for i in range(start, end + 1):
            if dp[i] == -inf: continue
            x, y = coords[i]
            for r, s, t in go_to[x * m + y]:
                j = index[(r, s)]
                dp[j] = max(dp[j], dp[i] + t)
                prefix[j] = max(prefix[j], dp[j] + a[r - 1] * (s - 1))
                suffix[j] = max(suffix[j], dp[j] + a[r - 1] * (m - s))
    print(-dp[-1] if dp[-1] != -inf else "NO ESCAPE")
