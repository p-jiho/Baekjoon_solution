case = int(input())
result = []
for _ in range(case):
    first, second = map(int, input().split())
    second_k = []
    for i in range(int(second**(1/2))+1):
        if second % (i+1) == 0:
            second_k.append(i+1)
            second_k.append(second//(i+1))
    second_k.sort()
    for s in second_k:
        if (first * s) % second == 0:
            result.append(first*s)
            break
for r in result:
    print(r)