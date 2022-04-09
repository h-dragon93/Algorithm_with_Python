import copy

def solution(d, budget):
    
    d.sort()
    tmpList = copy.deepcopy(d)
    cnt = 0
    
    for money in d :
        if tmpList[0] <= budget :
            budget -= tmpList.pop(0)
            cnt += 1
        else :
            break
            
    return cnt
