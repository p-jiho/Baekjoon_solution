n = list(map(int, input().split()))
m = [list(map(int, input().split())) for _ in range(n[1])]

one = []
for i in range(n[1]):
    a = [[i, j] for j in range(n[0]) if m[i][j] == 1]
    if len(a) != 0:
        one += a

depth = 0
while True:
    new_one = []
    for i, j in one:
        for new_i, new_j in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
            if new_i >= 0 and new_j >= 0 and new_i < n[1] and new_j < n[0] and m[new_i][new_j] == 0:
                new_one.append([new_i, new_j])
                m[new_i][new_j] = 1
    if len(new_one) == 0:
        break 
    else:
        one = new_one
        depth += 1

for i in range(n[1]):
    if 0 in m[i]:
        depth = -1
        break
print(depth)