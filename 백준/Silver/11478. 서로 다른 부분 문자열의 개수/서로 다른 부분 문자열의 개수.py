s = input()
result = []
for i in range(1,len(s)+1): 
    for j in range(len(s)):
        result.append(s[j:j+i])
print(len(set(result)))