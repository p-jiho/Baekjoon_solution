a = []
for n in range(5):
    a.append(int(input()))
a = sorted(a)
print(sum(a)//5)
print(a[2])