n = int(input())
result = [0]*n
result[0] = 1
if n != 1:
    result[1] = 3
    for i in range(2, n):
        result[i] = result[i-1] + 2*result[i-2]
print(result[n-1]%10007)