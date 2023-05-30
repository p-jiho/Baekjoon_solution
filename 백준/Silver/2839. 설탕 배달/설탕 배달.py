n = int(input())
s = []; i = 0
while(True):
    if (n-5*i)%3 == 0:
        s.append(i + (n-5*i)//3)
    i += 1
    if i != 0 and n < (5*i):
        break
if len(s) == 0:
    print(-1)
else:
    print(min(s))