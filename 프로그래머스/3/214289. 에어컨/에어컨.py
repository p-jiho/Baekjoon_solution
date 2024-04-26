def solution(temperature, t1, t2, a, b, onboard):
    min_t = min(abs(temperature - t1), abs(temperature - t2))
    max_t = max(abs(temperature -t1), abs(temperature - t2))
    temperature = 0
    m = 10**6
    table = [[m]*(max_t+1) for _ in range(len(onboard))]
    table[0][0] = 0
    for i in range(0, len(onboard)-1):
        case = onboard[i+1]
        for j in range(0, max_t+1):
            if table[i][j] == m:
                continue
            if case == 0:
                if j == 0:
                    table[i+1][j] = table[i][j]
                    table[i+1][j+1] = min(table[i][j] + a, table[i+1][j+1])
                elif j == max_t:
                    table[i+1][j-1] = min(table[i+1][j-1], table[i][j])
                    table[i+1][j] = min(table[i+1][j], table[i][j] + b)
                else:
                    table[i+1][j-1] = min(table[i+1][j-1], table[i][j])
                    table[i+1][j] = min(table[i+1][j], table[i][j] + b)
                    table[i+1][j+1] = min(table[i+1][j+1], table[i][j] + a)
            else:
                if j == min_t-1:
                    table[i+1][j+1] = min(table[i][j] + a, table[i+1][j+1])
                elif j == min_t:
                    table[i+1][j] = min(table[i][j] + b, table[i+1][j])
                    table[i+1][j+1] = min(table[i][j] + a, table[i+1][j+1])
                elif j == max_t:
                    table[i+1][j-1] = min(table[i+1][j-1], table[i][j])
                    table[i+1][j] = min(table[i+1][j], table[i][j] + b)
                elif min_t < j and j < max_t:
                    table[i+1][j-1] = min(table[i+1][j-1], table[i][j])
                    table[i+1][j] = min(table[i+1][j], table[i][j] + b)
                    table[i+1][j+1] = min(table[i+1][j+1], table[i][j] + a)
    return min(table[-1])