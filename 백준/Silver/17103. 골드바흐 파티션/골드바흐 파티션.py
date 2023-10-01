N = int(input())
cases = []
for _ in range(N):
    cases.append(int(input()))
m = max(cases)

result = [True]*m
result[0] = False
for i in range(int(m**0.5)+1):
    if result[i]:
        for j in range(2*i+1, m, i+1):
            result[j] = False

for case in cases:
    c = 0
    result_t = result[:case].copy()
    for i in range(case//2):
        if result_t[i] and result_t[case-i-2]:
            c += 1
    print(c)