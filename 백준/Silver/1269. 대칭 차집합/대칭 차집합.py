N, M = map(int, input().split())
first = set(map(int, input().split()))
second = set(map(int, input().split()))
inter = first & second
result = list(first - inter)
result += list(second - inter)
print(len(result))