def solution(s):
    stack = []
    
    for str in s :
        if str == "(" :
            stack.append(str)
        else :
            if not stack :
                stack.append(str)
            elif stack[-1] == ")" :
                stack.append(str)
            else :
                stack.pop()
    if not stack :
        return True
    else :
        return False
