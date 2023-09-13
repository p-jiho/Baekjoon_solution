import sys
input = sys.stdin.readline
N, M = map(int, input().split())
N_s = {}; M_s = []
for i in range(N):
    N_s[input()] = 1
a = 0
for i in range(M):
    try:
        N_s[input()]
    except KeyError:
        continue
    else:
        a += 1
print(a)