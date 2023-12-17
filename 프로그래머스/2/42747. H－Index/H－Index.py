def solution(citations):
    citations = sorted(citations, reverse = True)
    n = list(range(1, len(citations)+1))
    i = 0
    if citations[-1] >= len(citations):
        result = len(citations)
    else:
        while(True):
            if i >= len(citations):
                result = 0
                break
            elif citations[i] < n[i]:
                result = min(citations[i-1], n[i-1])
                break
            i += 1
    
    return result