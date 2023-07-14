num = int(input())
li = list(map(int, input().split()))
has_even = False
cnt = 0
for i in li:
    if i%2 == 0:
        has_even = True
    else:
        cnt+=1
if has_even and cnt:
    li.sort()
    print(' '.join(map(str, li)))
else:
    print(' '.join(map(str, li)))
