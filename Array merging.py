lengths = list(map(int,input().split()))
first_arr = list(map(int,input().split()))
second_arr = list(map(int, input().split()))
 
output = []
pointer_first = 0
pointer_second = 0
 
while pointer_first < lengths[0] and pointer_second < lengths[1]:
    if first_arr[pointer_first] < second_arr[pointer_second]:
        output.append(first_arr[pointer_first])
        pointer_first += 1
 
    else:
        output.append(second_arr[pointer_second])
        pointer_second += 1
 
 
if pointer_first < lengths[0]:
    output.extend(first_arr[pointer_first:])
 
if pointer_second < lengths[1]:
    output.extend(second_arr[pointer_second:])

print(*output)
