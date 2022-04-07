def solution(s):
    
    strList = list(s) 
    
    stack = []
    
    for i in range(len(s)) :
        if len(stack) > 0 :
            if stack[-1] == strList[i] :
                stack.pop()
            else :
                stack.append(strList[i])
        else :
            stack.append(strList[i])
            
    if len(stack) == 0 :
        answer = 1
    else :
        answer = 0

    return answer
