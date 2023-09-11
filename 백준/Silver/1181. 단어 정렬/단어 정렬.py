import sys

N = int(input())
M = []
for _ in range(N):
    s = input()
    M.append(s)
M = set(M)
M = [(len(s),s) for s in M]
M.sort()
M = [s for _, s in M]
print = sys.stdout.write
for a in M:
    print(str(a) + "\n")