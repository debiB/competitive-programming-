t = int(input())
for _ in range(t):
    size = int(input())
    arr = list(map(int, input().split()))
    is_valid = True
    arr.sort()
    for i in range(1,len(arr)):
        if abs(arr[i-1] - arr[i]) > 1:
            is_valid = False
            break
    if is_valid:
        print("YES")
    else:
        print("NO")
