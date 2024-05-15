def solution(m, n, puddles):
    matrix = [[1] * m for _ in range(n)]
    
    if puddles != [[]]:
        for y, x in puddles:
            matrix[x-1][y-1] = 0
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
                
            if [j + 1, i + 1] in puddles:
                continue
            
            if i == 0:
                matrix[0][j] = matrix[0][j-1]
            elif j == 0:
                matrix[i][0] = matrix[i-1][0]
            else:
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

    return matrix[-1][-1] % 1000000007