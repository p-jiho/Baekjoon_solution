def swing(lst):
    length = len(lst)
    new_key = [[0]*length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            new_key[j][length - 1 - i] = lst[i][j]
    return new_key

def check(lock_lst, check_start, check_last):
    result = True
    for i in range(check_start, check_last):
        if lock_lst[i][check_start:check_last] != [1]*(check_last - check_start):
            result = False
            return result
    return result

def lock_func(key_lst, lock_lst, idx_i, idx_j):
    for key_i in range(len(key_lst)):
        for key_j in range(len(key_lst)):
            lock_lst[idx_i + key_i][idx_j + key_j] = lock_lst[idx_i + key_i][idx_j + key_j] + key_lst[key_i][key_j]
    result = check(lock_lst, len(key_lst)-1, len(lock_lst) - len(key_lst)+1)
    return result

def solution(key, lock):
    length = len(key)
    new_length = len(lock) + len(key)*2 - 2
    
    for _ in range(4):
        for i in range(len(lock) + len(key) - 1):
            for j in range(len(lock) + len(key) - 1):
                plus1 = [[0] * new_length for _ in range(length - 1)]
                plus2 = [[0] * new_length for _ in range(length - 1)]
                new_lock = [[0]*(length - 1) + lock[i] + [0]*(length - 1) for i in range(len(lock))]
                new_lock = plus1 + new_lock + plus2
                result = lock_func(key, new_lock, i, j)
                if result == True:
                    return result
        key = swing(key)
    return result