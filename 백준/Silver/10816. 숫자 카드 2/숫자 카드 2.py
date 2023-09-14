N = int(input())
card = list(map(int, input().split()))
M = int(input())
test = list(map(int, input().split()))
card_d = {}
for i in range(N):
    try:
        card_d[card[i]]
    except:
        card_d[card[i]] = 1
    else:
        card_d[card[i]] += 1

result = []
for i in range(M):
    try:
        card_d[test[i]]
    except:
        result.append(0)
    else:
        result.append(card_d[test[i]])
print(*result)