test_n = 123456
test = list(range(1, 2*test_n+1))
for i in range(int(len(test)**(1/2) + 1)):
    if test[i] == 1:
        test[i] = 0
        continue

    if test[i] == 0:
        continue

    for j in range(i+1, len(test)):
        if test[j] % test[i] == 0:
            test[j] = 0
while(True):
    n = int(input())
    if n == 0:
        break
    result = test.copy()
    result = result[n:2*n]
    result = set(result)
    if n == 1:
        print(len(result))
    else:
        print(len(result)-1)