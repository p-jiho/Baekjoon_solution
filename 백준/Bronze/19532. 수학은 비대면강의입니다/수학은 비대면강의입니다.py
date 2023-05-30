a, b, c, d, e, f = map(int, input().split())
first = [a, b, c]
second = [d, e, f]
if d != 0 and a != 0:
    first = [d*first[i] for i in range(len(first))]
    second = [a*second[i] for i in range(len(second))]
    i = first[1] - second[1]
    y = (first[2] - second[2])//i
    x = (c - b*y)//a
elif d != 0:
    y = c//b
    x = (f - e*y)//d
elif a != 0:
    y = e//f
    x = (c - b*y)//a
print(x, y)