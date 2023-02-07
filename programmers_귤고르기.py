def solution(k, tangerine):
    
    target = 0
    count = 0
    sorted_dict = sorted(makeDict(tangerine).items(), key = lambda item: item[1], reverse = True)
    
    for tup in sorted_dict :
        target += tup[1]
        count += 1
        if target >= k :
            return count

def makeDict(tangerine) :
    dict = {}
    for tan in tangerine :
        if tan not in dict :
            dict[tan] = 1
        else :
            dict[tan] += 1
    return dict
