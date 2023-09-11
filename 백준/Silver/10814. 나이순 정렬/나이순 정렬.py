import sys

N = int(input())
M = []
for i in range(N):
    age, name = input().split()
    M.append((int(age), i,  name))
M.sort()
M = [(age, name) for age, _, name in M]
print = sys.stdout.write
for a, b in M:
    print(str(a) + " " + str(b) + "\n")