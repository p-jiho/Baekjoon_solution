result = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        del result[len(result)-1]
    else:
        result.append(x)

if len(result) == 0:
    print(0)
else:
    print(sum(result))