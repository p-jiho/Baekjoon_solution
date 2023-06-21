N = int(input()); a = []
for n in range(N):
    a.append(int(input()))
print(*sorted(list(set(a))), sep="\n")