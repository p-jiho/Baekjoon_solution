a, b = map(int, input().split())
c = int(input())
n = int(input())
if a > 0:
    if a*n + b <= c*n:
        if a == c:
            print(1)
        elif a*(b//(c-a)+2) + b <= c*(b//(c-a)+2):
            print(1)
        else:
            print(0)
    else:
        print(0)
else:
    if a*n +b <= c*n:
        print(1)
    else:
        print(0)