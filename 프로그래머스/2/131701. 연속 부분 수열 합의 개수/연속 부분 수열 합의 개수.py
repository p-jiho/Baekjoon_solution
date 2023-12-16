def solution(elements):
    result = [sum(elements)]
    l = len(elements)
    for i in range(len(elements)-1):
        elements += [elements[i]]
        for j in range(l):
            result += [sum(elements[j:j+i+1])]
    return len(set(result))