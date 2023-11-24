import numpy as np

def combi(lst, n):
    result = []
    if len(lst) == 1:
        result.append(lst)
        result.append([0])
    else:
        c_i = combi(lst[1:len(lst)], n)
        for c in c_i:
            result.append([lst[0]] + c)
            result.append([0] + c)
    return result




def solution(n, info):
    info_n = [i + 1 for i in info]

    result = combi(info_n[0:len(info_n)-1], n)
    result = [i + [n - sum(i)] if sum(i) < n else i + [0] for i in result]
    result = [i for i in result if sum(i) == n]

    i = 0
    score_r = []
    score_a = []

    for r in result:
        idx = np.nonzero(r)[0].tolist()
        score = sum([10 - i for i in idx])
        score_r.append(score)

        info_idx = np.nonzero(info)[0].tolist()
        info_idx = list(set(info_idx) - set(idx))
        score_info = sum([10 - i for i in info_idx])
        score_a.append(score_info)

    result_score = [score_r[i] - score_a[i] for i in range(len(score_r))]

    if max(result_score) <= 0:
        answer = [-1]
    else:
        if len(np.where(np.array(result_score) == max(result_score))[0]) == 1:
            answer = result[result_score.index(max(result_score))]
        else:
            p = np.where(np.array(result_score) == max(result_score))[0].tolist()
            print(p)
            result = [result[i] for i in p]

            for i in range(0, 11, -1):
                result.sort(key=lambda x: int(x[i]))

            answer = result[0]

    return answer
            

