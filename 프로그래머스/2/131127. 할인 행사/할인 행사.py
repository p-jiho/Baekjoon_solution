def solution(want, number, discount):
    n = 0
    
    for i in range(len(discount)-9):
        dis = discount[i:i+10]
        num = number.copy()

        for j in range(len(want)):
            if dis.count(want[j]) == number[j]:
                num[j] = 0
            else:
                break
                
        if sum(num) == 0:
            n += 1
    return n