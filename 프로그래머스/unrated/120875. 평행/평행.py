def solution(dots):
    # from itertools import combinations, permutations을 쓰지 않는 방법
    result = 0
    x = dots[0]
    for i in range(1, len(dots)):
        y = dots[i]
        new_dots = dots[1:].copy()
        del new_dots[i-1]
        a, b = new_dots
        if (x[0] - y[0])/(a[0] - b[0]) == (x[1] - y[1])/(a[1] - b[1]):
            result = 1
            break
    return result