import sys
a = [0]*10001
input = sys.stdin.readline
N = int(input())

for _ in range(N):
    w = int(input())
    a[w] += 1

for i in range(len(a)):
    for j in range(a[i]):
        print(i)