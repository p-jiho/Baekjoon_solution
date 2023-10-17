N = int(input())

for _ in range(N):
    v = list(str(input()))
    result = []

    for i in v:
        if result == [] and i == ")":
            result = 0
            break
        elif i == "(":
            result.append("(")
        elif i == ")":
            del result[len(result)-1]

    if type(result) == int:
        print("NO")
    elif len(result) == 0:
        print("YES")
    else:
        print("NO")