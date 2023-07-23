n, m = map(int, input().split())
matrix = [[0 for _ in range(m)] for _ in range(n)]
ans = ''
for i in range(n):
    l = input()
    for j in range(m):
        matrix[i][j] = l[j]
for i in range(n):
    for j in range(m):
        is_dup = False
        k = 0
        while k < n:
            if k != i and matrix[k][j] == matrix[i][j]:
                is_dup = True
                break
            k += 1

        l = 0
        while l < m:
            if l != j and matrix[i][l] == matrix[i][j]:
                is_dup = True
                break
            l += 1

        if not is_dup:
            ans += matrix[i][j]

print(ans)

