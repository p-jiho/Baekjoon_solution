def solution(triangle):
    for i in range(len(triangle)):
        # 꼭대기는 건너뜀
        if i == 0:
            continue
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                left = triangle[i-1][j]
                right = triangle[i-1][j-1]
                now = triangle[i][j]
                triangle[i][j] = max(now + left, now + right)
                
    return max(triangle[-1])