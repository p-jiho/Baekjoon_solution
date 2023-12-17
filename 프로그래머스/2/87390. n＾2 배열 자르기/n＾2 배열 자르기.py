def solution(n, left, right):
    left1 = left // n
    left2 = left % n
    right1 = right // n
    right2 = right % n
    result = []
    for i in range(left1, right1+1):
        if i == left1:
            if left1 < left2:
                result += list(range(left2+1, n+1))
            else:
                result += [left1+1]*(left1 - left2)
                result += list(range(left1+1, n+1))
        else:
            result += [i+1]*(i)
            result += list(range(i+1, n+1))
    return result[0:right-left+1]