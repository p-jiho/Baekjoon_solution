import re
def solution(s):
    all = [s]
    for i in range(1, len(s)):
        all += [s[i:]+s[:i]]
    n = 0
    for i in all:
        while(True):
            if i == "":
                n += 1
                break
            if re.search(r"\(\)|\{\}|\[\]", i) == None:
                break
            i = re.sub(r"\(\)|\{\}|\[\]", "", i)
        
    
    return n