
N, M = map(int, input().split())
N_s = {}; M_s = []
for i in range(N):
    s = input()
    N_s[s] = str(i+1)
    N_s[str(i+1)] = s
result = []
for _ in range(M):
    result.append(N_s[str(input())])
    
for res in result:
    print(res)