def solution(s):
    
    answer=[]
    tmp = []
    
#   문제 조건에 따라 정렬 후 차집합 구하기 위해 
    splited = s[2:-2].split('},{')
    splited.sort(key = lambda x : len(x))
    
    for str in splited :
        tmp.append(str.split(','))
        
#   시작 값 세팅
    answer.append(int(tmp[0][0]))
    
#   차집합 이용 위해 set으로 변환후 다시 list 
    for i in range(len(tmp)-1) :
        test = list(set(tmp[i+1]) - set(tmp[i]))
        answer.append(int(test[0]))
        
    return answer
