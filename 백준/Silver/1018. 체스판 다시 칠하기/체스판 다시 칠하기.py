n, m = map(int, input().split())
if m % 2 == 0:
    w = ["W", "B"]*(m//2)
    b = ["B", "W"]*(m//2)
else:
    w = ["W", "B"]*(m//2) + ["W"]
    b = ["B", "W"]*(m//2) + ["B"]
    
case1 = [[0 for j in range(m)] for i in range(n)]
case2 = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    chess = list(input())
    
    if i % 2 == 0:
        case1[i] = [chess[j] != w[j] for j in range(m)]
        case2[i] = [chess[j] != b[j] for j in range(m)]
    else:
        case1[i] = [chess[j] != b[j] for j in range(m)]
        case2[i] = [chess[j] != w[j] for j in range(m)]

result = n*m
row = 0; col = 0
for row in range(n-7):
    for col in range(m-7):
        s1 = 0; s2 = 0
        for i in range(row, row+8):
            s1 += sum(case1[i][col:col+8])
            s2 += sum(case2[i][col:col+8])
        if result >= s1 and s2 >= s1:
            result = s1
        elif result > s2 and s1 > s2:
            result = s2
print(result)