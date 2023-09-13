import sys
input = sys.stdin.readline
N = int(input())
log = {}
for i in range(N):
    name, record = input().split()
    try:
        log[name]
    except KeyError:
        log[name] = record
    else:
        del log[name]
names = list(log.keys())
names.sort(reverse=True)
print = sys.stdout.write
for name in names:
    print(name + "\n")