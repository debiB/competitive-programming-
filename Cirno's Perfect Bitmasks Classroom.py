t = int(input())
for _ in range(t):
    num = int(input())
    
    s = bin(num)[2:]
    if s.count('1') > 1:
        k = 0 
        while not((num>>k) & 1):
            k += 1
        
        print(2**k)
        
    else:
        k = 0 
        while not((num>>k) & 1):
            k += 1
        
        if not k :
            print(3)
        
        else:
            print(2**k + 1)
