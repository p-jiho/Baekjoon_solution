import sys

input = sys.stdin.readline
N = int(input())
x = []
for _ in range(N):
    n = list(map(int, input().split()))
    if n[0] == 1:
        x.append(n[1])
    elif n[0] == 2:
        if len(x) == 0:
            print(-1)
        else:
            print(x[len(x)-1])
            del x[len(x)-1]
    elif n[0] == 3:
        print(len(x))
    elif n[0] == 4:
        if len(x) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(x) == 0:
            print(-1)
        else:
            print(x[len(x)-1])
