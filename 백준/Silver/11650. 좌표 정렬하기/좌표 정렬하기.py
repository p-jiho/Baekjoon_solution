N = int(input())
M = []
for _ in range(N):
    a, b = map(int, input().split())
    M.append((a, b))
M.sort()
import sys
print = sys.stdout.write
for a, b in M:
    print(str(a) + " " + str(b) + "\n")
