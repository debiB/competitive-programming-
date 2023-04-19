from collections import defaultdict
inp = int(input())
dic = defaultdict(list)
for i in range(inp):
    row = list(map(int, input().split()))

    for j in range(len(row)) :
        if row[j] == 1:
            dic[i+1].append(j+1)
for key,value in dic.items():
    print(f"{len(value)}", end = " ")
    for j in range (len(value)):
        print(f"{value[j]}", end = " ")
    print()
