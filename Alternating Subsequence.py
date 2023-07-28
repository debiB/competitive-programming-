t = int(input())
for _ in range(t):
    size = int(input())
    li = list(map(int, input().split()))
    s = 0
    k = 0
    
    while k < size:
        _max_pos = float("-inf")
        j = k
        while j < size and li[j] > 0:
            _max_pos = max(_max_pos, li[j])
            j += 1
        if _max_pos != float("-inf"):  # If any positive number found
            s += _max_pos
        
        _max_neg = float("-inf")
        k = j
        while k < size and li[k] < 0:
            _max_neg = max(_max_neg, li[k])
            k += 1
        if _max_neg != float("-inf"):  # If any negative number found
            s += _max_neg

    print(s)
