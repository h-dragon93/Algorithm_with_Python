def solution(string) :
    str_li = list(string)
    case_num = len(str_li)
    stack = []
    for i in range(case_num) :
        if not stack or stack[-1] != str_li[i] :
            stack.append(str_li[i])
        elif stack and stack[-1] == str_li[i] :
            stack.pop()
    return len(stack)

T = int(input())
for test_case in range(1, T+1) :
    string = input()
    print('#{0} {1}'.format(test_case, solution(string)))
