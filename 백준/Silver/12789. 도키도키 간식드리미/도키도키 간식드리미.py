
N = int(input())
x = list(map(int, input().split()))
x_n = []
j = 1
while(True):
    if len(x) == 0 and len(x_n) == 0:
        break
    elif len(x) == 0 and x_n[-1] > j:
        break

    if len(x) > 0 and x[0] == j:
        del x[0]
        j += 1
    elif len(x_n) > 0 and x_n[-1] == j:
        del x_n[-1]
        j += 1
    else:
        x_n.append(x[0])
        del x[0]

if len(x_n) == 0:
    print("Nice")
else:
    print("Sad")