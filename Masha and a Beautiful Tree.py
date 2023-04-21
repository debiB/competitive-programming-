
def merge(left, right, arr):
    if left == right:
        return [arr[left]],0
    mid = left+ (right - left)//2
    l, op_l = merge(left, mid, arr)
    r, op_r = merge(mid+1,right, arr)
    if l[0] > r[0]:
        return r + l, op_l + op_r + 1
    else:
        return l + r, op_l + op_r
num = int(input())
for i in range(num):
    n = int(input())
    li = list(map(int, input().split()))
    arr, o = merge(0, len(li)-1,li)
    indi = 1
    for j in range(1,len(arr)):
        if arr[j] < arr[j-1] :
            indi = 0
            break
    if indi:
        print(o)
    else:
        print(-1) 
