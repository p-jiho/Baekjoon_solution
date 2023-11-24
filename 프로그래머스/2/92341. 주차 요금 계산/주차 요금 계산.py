def solution(fees, records):
    
    # 입/출차 기록 정리
    records_dict = {}
    records_lst = []
    for record in records:
        time, number, in_out = record.split()
        h, m = time.split(":")
        time = int(h) * 60 + int(m)
        records_dict[number] = 0
        records_lst.append([time, number, in_out])
        
    number = []
    for record in records_lst:
        if record[2] == "IN":
            number.append(record[1])
            records_dict[record[1]] -= record[0]
        elif record[2] == "OUT":
            del number[number.index(record[1])]
            records_dict[record[1]] += record[0]
    
    if len(number) != 0:
        for n in number:
            records_dict[n] += 23*60 + 59
    number = list(records_dict.keys())
    number.sort()
    
    
    answer = []
    for num in number:
        if records_dict[num] <= fees[0]:
            answer.append(fees[1])
        else:
            if (records_dict[num] - fees[0]) % fees[2] == 0:
                fee = fees[1] + (records_dict[num] - fees[0])//fees[2]*fees[3]
            else:
                fee = fees[1] + ((records_dict[num] - fees[0])//fees[2] + 1) * fees[3]
            answer.append(fee)

    return answer
