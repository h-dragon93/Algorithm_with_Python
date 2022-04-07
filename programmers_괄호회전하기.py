def solution(s):
    
    answer = 0
    strList = list(s)
    
    for _ in range(len(strList)) :
        stack = []
        for i in range(len(strList)) :
#         길이가 0이 아니면 체크 
            if len(stack) >0 :
                if stack[-1] == "(" and strList[i]==")":
                    stack.pop()
                elif stack[-1] =="[" and strList[i]=="]":
                    stack.pop()
                elif stack[-1] == "{" and strList[i]=="}":
                    stack.pop()
#                 만약에 마지막에 있는 문자가 다르면 추가    
                else:
                    stack.append(strList[i])
#         길이가 0이면 추가
            else:
                stack.append(strList[i])
        if len(stack) == 0:
            answer+=1
#         첫번째꺼 맨뒤로 보내고 반복
        strList.append(strList.pop(0))
    
    return answer
