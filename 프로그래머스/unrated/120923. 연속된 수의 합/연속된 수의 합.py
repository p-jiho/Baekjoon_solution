def solution(num, total):
    first = (total*2//num-num+1)//2
    return list(range(first, first+num))