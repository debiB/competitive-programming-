inp = int(input())
roads = set()
for i in range(inp):
    row= list(map(int, input().split()))
    for j in range(len(row)):
        if (i,j) not in roads and row[j]:
            roads.add((i,j))
print(len(roads)//2)
