def solution(sequence):
    global result
    
    for i in range(len(sequence)):
        if i % 2 == 1:
            sequence[i] = -sequence[i]
    
    lst = []
    if sequence[0] >= 0:
        sign = 0
    else:
        sign = 1
    
    total = sequence[0]
    
    if len(sequence) == 1:
        lst.append(abs(total))

    for i in range(1, len(sequence)):
        if sequence[i] >= 0 and sign == 1:
            lst.append(total)
            total = sequence[i]
            sign = 0
        elif sequence[i] < 0 and sign == 0:
            lst.append(total)
            total = sequence[i]
            sign = 1
        else:
            total += sequence[i]
        
        if i == len(sequence) - 1:
            lst.append(total)
    
    dp1 = [0] * len(lst)
    dp2 = [0] * len(lst)
    
    for i in range(len(lst)):
        if i == 0:
            dp1[0] = lst[0]
            dp2[0] = lst[0]
        else:
            dp1[i] = max(dp1[i-1] + lst[i], lst[i])
            dp2[i] = min(dp2[i-1] + lst[i], lst[i])

    return max(max(dp1), abs(min(dp2)))
