inp = int(input())
li = []
source = []
sink = []
for i in range(inp):
    li.append(list(map(int, input().split())))
    if max(li[i]) == 0:
        sink.append(i+1)
m =0
for a in range(len(li[0])):
    for b in range(len(li)):
        m = max(li[b][a], m)
    if m == 0:
        source.append(a+1)
    m = 0
print(len(source), *source)
print(len(sink), *sink)
