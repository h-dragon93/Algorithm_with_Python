def calculation(oper_list) :
    final_list = []
    for oper in oper_list :
        if oper[0] == "I" :
            final_list.append(int(oper[1]))
            final_list.sort()
        elif oper[0] == "D" :
            if len(final_list) == 0:
                continue
            elif oper[1] == "1" :
                final_list.pop()
            elif oper[1] == "-1" :
                final_list.pop(0)
    if len(final_list) == 0 :
        return [0,0]
    else :
        return [max(final_list),min(final_list)]

def solution(operations):
    oper_list = []
    for i in operations :
        oper_list.append(i.split(" "))
    answer = calculation(oper_list)
    return answer
