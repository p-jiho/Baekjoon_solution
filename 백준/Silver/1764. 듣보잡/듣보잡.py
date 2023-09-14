N, M = map(int, input().split())
li = []
lo = []
for _ in range(N):
    li.append(input())
for _ in range(M):
    lo.append(input())
li = set(li); lo = set(lo)
result = list(li & lo)
result.sort()

print(len(result))
for re in result:
    print(re)