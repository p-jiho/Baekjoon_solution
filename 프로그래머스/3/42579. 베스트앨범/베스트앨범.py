def solution(genres, plays):
    result_dict = {}
    for i in range(len(genres)):
        if genres[i] not in result_dict.keys():
            result_dict[genres[i]] = [plays[i], [i]]
        else:
            result_dict[genres[i]][0] += plays[i]
            result_dict[genres[i]][1].append(i)
    
    best_score = []
    for key in result_dict.keys():
        best_score.append(result_dict[key][0])

    best_genres = []
    for i in sorted(best_score, reverse=True):
        best_genres.append(list(result_dict.keys())[best_score.index(i)])
   
    result = []
    for genre in best_genres:
        idx = result_dict[genre][1]
        

        if len(idx) == 1:
            result.append(idx[0])
            continue

        score = [plays[i] for i in idx]        
        for _ in range(2):
            result.append(idx[score.index(sorted(score)[-1])])
            score[score.index(sorted(score)[-1])] = 0
        
    return result