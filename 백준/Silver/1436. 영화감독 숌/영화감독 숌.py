n = int(input())
i = 1
result = []
while(True):
    for j in range(i+1):
        t = list(range(0,10))
        for _ in range(i-1):
            a = []
            for o in range(len(t)):
                a += [str(t[o]) + str(w) for w in range(0,10)]
            t = a.copy()
            
        for k in range(len(t)):
            q = list(str(t[k]))
            q.insert(j, "666")
            result += [int("".join(q))]
    i += 1
    if len(result) > n:
        break
        

result = list(set(result))
result.sort()
print(result[n-1])