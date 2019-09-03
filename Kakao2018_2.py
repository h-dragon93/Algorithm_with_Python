def solution(N, stages):
    stageNum = N
    inputSize = len(stages)
    total = 0; notClear = 0; tmp = [] ; ans = [] ; final = []
    for k in range(1, stageNum+1) :
        for i in range(inputSize) :
            if stages[i] >= k :
                total += 1
            if stages[i] == k :
                notClear += 1
        if max(stages) < k :
            tmp.append(0)                 
        else :
            tmp.append(notClear/total)
        total=0; notClear=0
    for i, rate in enumerate(tmp) :
        ans.append([i+1, rate])
    sortedTmp = sorted(tmp, reverse=True)
    for i in range(stageNum) :
        for j in range(len(ans)) :
            if sortedTmp[i] == ans[j][1] :
                final.append(ans[j][0])
                ans.pop(j)
                break
    return final
