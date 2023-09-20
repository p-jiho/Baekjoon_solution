N = int(input())
for _ in range(N):
    n = int(input())
        
    while(True):
        if n == 1 or n == 0:
            n += 1
            continue
        
        a = 0
        n_c = round(n**(1/2))+1
        if n_c == n:
            print(n)
            break 
            
        for i in range(2, n_c+1):
            if i != 2 and i % 2 == 0:
                continue
            elif n % i == 0:
                a = 1
                break
            else:
                continue
        if a == 0:
            print(n)
            break
        else:
            n += 1