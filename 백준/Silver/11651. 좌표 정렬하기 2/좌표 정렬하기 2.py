import sys

N = int(input())
M = []
for _ in range(N):
    a, b = map(int, input().split())
    M.append((b, a))
M.sort()
M = [(b, a) for a, b in M]
print = sys.stdout.write
for a, b in M:
    print(str(a) + " " + str(b) + "\n")