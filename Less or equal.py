n, k = map(int, input().split())

arr = sorted(list(map(int, input().split())))


if k == 0:
    if arr[0] >= 2:
        print(1)
    else:
        print(-1)

elif k == n:
    print(arr[k-1])
    exit()
    
elif arr[k-1] == arr[k]:
    print(-1)
    
else:
    print(arr[k-1]) 
    
