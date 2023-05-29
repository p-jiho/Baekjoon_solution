a, b = map(int, input().split())
c = int(input())
n = int(input())
if a > 0 and a*n + b <= c*n:
    if a <= c:
        print(1)
    else:
        print(0)
elif a <= 0 and a*n + b <= c*n:
    print(1)
else:
    print(0)