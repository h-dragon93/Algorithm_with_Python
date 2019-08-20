def solution(li) :
    stack = []
    N = len(li)
    operand = ['+', '-', '/', '*', '.']
    for i in range(N) :
        if li[i] not in operand :
            stack.append(li[i])
        elif li[i] in operand and li[i] != '.' :
            if len(stack) <= 1 :
                return "error"
            b = int(stack.pop())
            a = int(stack.pop())
            if   li[i] == '+' :
                stack.append(a+b)
            elif li[i] == '-' :
                stack.append(a-b)
            elif li[i] == '*' :
                stack.append(a*b)
            elif li[i] == '/' :
                stack.append(a//b)
        elif li[i] == '.' :
            if len(stack) > 1 :
                return "error"
            return stack[0]

T = int(input())
for test_case in range(1, T+1) :
    input_li = input().split()
    print('#{0} {1}'.format(test_case, solution(input_li)))
