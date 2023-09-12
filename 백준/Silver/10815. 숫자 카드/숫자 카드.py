import sys
input = sys.stdin.readline
N = int(input())
N_d = dict(zip(list(map(int, input().split())), [1]*N))
M = int(input())
M_d = list(map(int, input().split()))
print = sys.stdout.write
for i in range(M):
    try:
        N_d[M_d[i]]
    except KeyError:
        print(str(0) + " ")
    else:
        print(str(1) + " ")