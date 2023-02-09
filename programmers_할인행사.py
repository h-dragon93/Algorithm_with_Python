def solution(want, number, discount):
    answer = 0
    originDict = makeDict(want, number)
    target = sum(originDict.values())
    for i in range(len(discount)-target+1) :
        compareDict = makedict(discount[i:i+target])
        if compareDict == originDict :
            answer += 1
    
    return answer

def makedict(list) :
    tmpDict = dict()
    for i in range(len(list)) :
        if list[i] not in tmpDict :
            tmpDict[list[i]] = 1
        else :
            tmpDict[list[i]] += 1
            
    return tmpDict

def makeDict(want, number) :
    wantDict = dict()
    for i in range(len(want)) :
        wantDict[want[i]] = number[i]
        
    return wantDict
