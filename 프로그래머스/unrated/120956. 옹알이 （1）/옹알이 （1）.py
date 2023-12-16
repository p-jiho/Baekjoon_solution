def solution(babbling):
    str = ["aya", "ye", "woo", "ma"]
    n = 0
    for x in babbling:
        for y in str:
            if len(x.split(y)) > 2:
                break
            x = x.replace(y, " ")
        
        if len(x.replace(" ", "")) == 0:
            n += 1
            
    return n

