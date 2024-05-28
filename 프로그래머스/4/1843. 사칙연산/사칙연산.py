def check(start, i, num, min_n, max_n):
    l = i - start + 1
    m = [[0]*l for _ in range(l)]

    for j in range(l):
        for k in range(j, l):
            if j == 0 and k == 0:
                m[0][0] = -num[i]
                continue

            if j == k:
                m[j][j] = m[j-1][j-1] - num[i-k]
            else:
                m[k][j] = m[k-1][j] + num[i-k]

    result = []
    for j in m[-1]:
        if len(m[-1]) == 1:
            result.append(j-min_n)
            result.append(j+min_n)
            result.append(j-max_n)
            result.append(j+max_n)
            continue
            
        
        if j == m[-1][-1]:
            result.append(j-min_n)
            result.append(j-max_n)
        
        result.append(j+min_n)
        result.append(j+max_n)
        

    min_n = min(result)
    max_n = max(result)
    return min_n, max_n



def solution(arr):
    oper = []
    num = []
    for i in range(len(arr)-1, -1, -1):
        if i % 2 == 0:
            num.append(int(arr[i]))
        else:
            oper.append(arr[i])
    
    min_n = 0
    max_n = 0
    start = 0
    minus = -1
    for i in range(len(oper)):
        if oper[i] == "-":
            min_n, max_n = check(start, i, num, min_n, max_n)
            start = i + 1
            minus = i

    s = sum(num[minus+1:])
    max_n = max(s+min_n, s+max_n)
    return max_n