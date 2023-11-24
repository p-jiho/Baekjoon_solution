
def solution(info, edges):
    v = [0]*len(info)
    answer = []

    def logic(s, w):
        if s > w:
            answer.append(s)
        else:
            return

        for a, b in edges:
            if v[a] and not v[b]:
                v[b] = 1
                if info[b] == 0:
                    logic(s + 1, w)
                else:
                    logic(s, w+1)
                v[b] = 0
    v[0] = 1
    logic(1,0)
    return max(answer)
                
            