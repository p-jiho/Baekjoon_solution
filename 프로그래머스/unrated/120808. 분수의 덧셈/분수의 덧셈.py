def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer = numer1 * denom2 + numer2 * denom1
    mi = min(denom, numer)
    ma = max(denom, numer)
    m = []
    for i in range(1, int(mi**(1/2))+1):
        if mi % i == 0:
            m.append(i)
            m.append(mi // i)
    
    n = 0
    m = sorted(m, reverse=True)
    i = 0
    
    while(True):
        if n != 0:
            break
        if ma % m[i] == 0:
            n = m[i]
        i += 1
    denom = denom // n
    numer = numer // n
    
            
        
    
    
    return [numer, denom]