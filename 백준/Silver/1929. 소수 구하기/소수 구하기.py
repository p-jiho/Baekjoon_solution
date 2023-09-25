m, n = map(int, input().split())

for i in range(m, n+1):
    if i == 1:
        continue
    a = 0
    i_r = round(i**(1/2))
    for j in range(2, i_r+1):
        if i % j == 0:
            a = 1
            break
    if a == 0:
        print(i)