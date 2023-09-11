import sys
input = sys.stdin.readline
N = int(input())
M = list(map(int, input().split()))
s = list(set(M))
s.sort()

d = dict(zip(s, list(range(len(s)))))
print = sys.stdout.write
for i in M:
    print(str(d[i])+ " ")