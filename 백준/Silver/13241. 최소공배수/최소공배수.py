first, second = map(int, input().split())
f = first
s = second
while(s > 0):
    f, s = s, f % s
print(first * second // f)