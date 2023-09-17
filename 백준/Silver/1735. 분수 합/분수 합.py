f_up, f_down = map(int, input().split())
s_up, s_down = map(int, input().split())
f = f_down
s = s_down
while(s > 0):
    f, s = s, f % s
m_d = f_down * s_down // f
f_up = f_up * m_d // f_down
s_up = s_up * m_d // s_down
up = f_up + s_up

u = up
d = m_d
while(d > 0):
    u, d = d, u % d
result = [up // u, m_d // u]
print(*result)