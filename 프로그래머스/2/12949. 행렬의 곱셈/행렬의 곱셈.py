def solution(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        r = []
        for k in range(len(arr2[0])):
            a = 0
            for j in range(len(arr1[i])):
                a += arr1[i][j]*arr2[j][k] 
            r.append(a)
        result.append(r)
    return result