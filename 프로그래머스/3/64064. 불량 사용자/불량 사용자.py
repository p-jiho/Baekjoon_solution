def check_fuc(depth, lst):
    global id_lst, num

    for i in id_lst[depth]:
        if i not in lst:
            if depth == len(id_lst) - 1:
                new_lst = lst.copy()
                #print(new_lst, i)
                new_lst.append(i)
                num.append(new_lst)
            else:
                new_lst = lst.copy()
                new_lst.append(i)
                check_fuc(depth + 1, new_lst)
    return
            
def solution(user_id, banned_id):
    global id_lst, num
    id_lst = []
    for ban in banned_id:
        value = []
        size = len(ban)
        for user in user_id:
            if len(user) != size:
                continue
            
            check = 0
            for idx in range(size):
                if ban[idx] == "*":
                    continue
                elif ban[idx] == user[idx]:
                    continue
                else:
                    check = 1
                    break
            if check == 0:
                value.append(user)

        id_lst.append(value)
    num = []
    result = []
    if len(banned_id) == 1:
        return len(id_lst[0])
    for i in id_lst[0]:
        result.append(check_fuc(1, [i]))
    return len(set([tuple(sorted(i)) for i in num]))