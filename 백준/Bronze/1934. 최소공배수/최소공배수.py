case = int(input())
result = []
for _ in range(case):
    first, second = map(int, input().split())
    second_k = []
    if second % 2 == 0:
        for i in range(second//2):
            if second % (i+1) == 0:
                second_k.append(i+1)
                second_k.append(second//(i+1))
    else:
        for i in range(second//2+1):
            if second % (i+1) == 0:
                second_k.append(i+1)
                second_k.append(second // (i + 1))
    second_k.sort()
    for s in second_k:
        if (first * s) % second == 0:
            result.append(first*s)
            break
for r in result:
    print(r)