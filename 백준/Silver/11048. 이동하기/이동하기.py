N, M = map(int, input().split())
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))

result = [[0]*M for _ in range(N)]
result[0][0] = lst[0][0]

for i in range(1, N):
    result[i][0] = result[i-1][0] + lst[i][0]

for j in range(1, M):
    result[0][j] = result[0][j-1] + lst[0][j]

for i in range(1, N):
    for j in range(1, M):
        result[i][j] = max(result[i-1][j], result[i][j-1]) + lst[i][j]
print(result[N-1][M-1]) 
