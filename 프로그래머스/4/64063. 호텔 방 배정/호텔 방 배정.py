import sys
sys.setrecursionlimit(10**6)
def check(room_lst, index, l, k):
    new_i = room_lst[index]
    l.append(new_i)
    if new_i not in room_lst.keys():
        for j in l:
            room_lst[j] = new_i + 1
        return room_lst, new_i
    else:
        return check(room_lst, new_i, l, k)
def solution(k, room_number):
    room = {}
    result = []
    for i in room_number:
        if i not in room.keys():
            room[i] = i + 1
        else:
            lst = [i]
            room, i = check(room, i, lst, k)
        result.append(i)
    return result