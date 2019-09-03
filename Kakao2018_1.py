def solution(record):
    inputSize = len(record)
    inputList = []
    uidDict = {}
    answer = []
    for i in range(inputSize) :
        inputList.append(record[i].split())
    for i in range(inputSize) :
        if inputList[i][0] != "Leave" :
            uidDict[inputList[i][1]] = inputList[i][2]
    for i in range(inputSize) :
        Name = uidDict[inputList[i][1]]
        if inputList[i][0] == "Enter" :
            answer.append("{0}님이 들어왔습니다.".format(Name))
        elif inputList[i][0] == "Leave" :
            answer.append("{0}님이 나갔습니다.".format(Name))
    return answer
