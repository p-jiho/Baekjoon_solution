n = list(input())
s = int("".join(n)) - (9*(len(n)-1)+int(n[0])-1)
i = s; result = 0
while(i <= int("".join(n))):
    if i + sum(map(int, str(i))) == int("".join(n)):
        result = i
        break
    i += 1
print(result)