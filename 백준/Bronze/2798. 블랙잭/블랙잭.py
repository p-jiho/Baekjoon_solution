n, stan = map(int, input().split())
card = list(map(int, input().split()))
result = []
s_lst = [0]*3
def last(x):
    for i in range(s_lst[1], n):
        s_lst[2] = i
    return sum(s_lst)

def s(x):
    global s_lst
    if x == 3:
        r = card[s_lst[0]] + card[s_lst[1]] + card[s_lst[2]]
        if r <= stan:
            
            result.append(r)
        return

    if x == 0:
        for i in range(n-2):
            s_lst[0] = i
            s(x+1)
    elif x == 1:
        for i in range(s_lst[0]+1, n-1):
            s_lst[1] = i
            s(x+1)
    elif x == 2:
        for i in range(s_lst[1]+1, n):
            s_lst[2] = i
            s(x+1)
            
s(0)
print(max(result))