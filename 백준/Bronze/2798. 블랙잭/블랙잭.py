n, m = map(int, input().split())
card = list(map(int, input().split()))
ma = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j != k != i:
                s = card[i] + card[j] + card[k]
                if ma < s and s <= m:
                    ma = s
print(ma)