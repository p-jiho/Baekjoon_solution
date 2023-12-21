def solution(clothes):
    cloth_dict = {}
    for _, y in clothes:
        cloth_dict[y] = []
    
    for x, y in clothes:
        cloth_dict[y].append(x)
    
    result = 1
    for key in list(cloth_dict.keys()):
        result *=  len(cloth_dict[key])+1
    
    return result - 1