def makeReportedId(report, reportedIdMap) :

    for str in report :
        tmp = str.split(' ')
        if reportedIdMap[tmp[0]] == None :
            reportedIdMap[tmp[0]] = [tmp[1]]
        else :
            reportedIdMap[tmp[0]].append(tmp[1])

    return reportedIdMap

def deleteDup(report) :
    return list(set(report))

def makeReportList(reportMap, k) :
    
    countDic = {}
    reportedList = []
    
    for key, value in reportMap.items() :
        if value == None :
            continue
        for user in value :
            if user not in countDic :
                countDic[user] = 1
            else :
                countDic[user] += 1

    for key, value in countDic.items() :
        if value >= k :
            reportedList.append(key)
            
    return reportedList

def makeAnswer(reportMap,reportedList, answer) :

    for id in reportMap :
        if reportMap[id] == None :
            answer.append(0)
            continue
        tmpInt = 0
        for target in reportMap[id] :
            if target in reportedList :
                tmpInt += 1
        answer.append(tmpInt)
        
    return answer


def solution(id_list, report, k):
    
    answer = []
    reportedIdMap = dict.fromkeys(id_list)
    report = deleteDup(report)
    reportMap = makeReportedId(report, reportedIdMap)
    reportedList = makeReportList(reportMap, k)
    answer = makeAnswer(reportMap,reportedList, answer)

    return answer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

    #id_list = ["con", "ryan"]
    #report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k = 2

    solution(id_list, report, k)
