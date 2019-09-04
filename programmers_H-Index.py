def solution(citations):
    h= max(citations)
    if max(citations) == 0 :
        return 0
    while h > 0 :
        count_up = 0
        count_down = 0
        for i in range(len(citations)) :
            if citations[i] >= h :
                count_up += 1
            else :
                count_down += 1
        if count_up >= h and count_down <= h :
            return h
        h -= 1
