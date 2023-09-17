import sys
input = sys.stdin.readline
N = int(input())
case = []
for _ in range(N):
    case.append(int(input()))
case_s = [s - f for f, s in zip(case[:len(case)-1], case[1:])]
case_s = list(set(case_s))

m = case_s[0]
case_s = case_s[1:len(case_s)]

i = 0
while(len(case_s)>0):
    f_t = case_s[i]
    case_s = list(set([x for x in case_s if x % m != 0]))
    c = []
    s_t = m
    c.append(f_t)
    while(s_t > 0):
        f_t, s_t = s_t, f_t % s_t
    m = f_t

result = (max(case) - min(case))//m+1-len(case)
print(result)