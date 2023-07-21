def inbound(i, j, r, c):
    return 0 <= i < r and 0 <= j < c

t = int(input())

for _ in range(t):
    r, c = map(int, input().split())
    li = []
    for _ in range(r):
        li.append(list(map(int, input().split())))
    max_sum = 0

    for i in range(r):
        for j in range(c):
            _sum = 0
            # Calculate sum in the forward diagonal (bottom-right direction)
            row, col = i + 1, j + 1
            while inbound(row, col, r, c):
                _sum += li[row][col]
                row += 1
                col += 1

            # Calculate sum in the backward diagonal (bottom-left direction)
            row, col = i + 1, j - 1
            while inbound(row, col, r, c):
                _sum += li[row][col]
                row += 1
                col -= 1

            # Calculate sum in the backward diagonal (top-left direction)
            row, col = i - 1, j - 1
            while inbound(row, col, r, c):
                _sum += li[row][col]
                row -= 1
                col -= 1

            # Calculate sum in the forward diagonal (top-right direction)
            row, col = i - 1, j + 1
            while inbound(row, col, r, c):
                _sum += li[row][col]
                row -= 1
                col += 1

            _sum += li[i][j]
            max_sum = max(max_sum, _sum)

    print(max_sum)
