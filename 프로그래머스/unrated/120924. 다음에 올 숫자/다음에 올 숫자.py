def solution(common):
    x = common[1] - common[0]
    if common[0] != 0:
        y = common[1] // common[0]
    else:
        y = 0
        
    if common[2] == common[1] + x:
        result = common[len(common) - 1] + x
    elif common[2] == common[1] * y:
        result = common[len(common) - 1] * y
    return result