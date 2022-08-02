def solution(arr):
    answer = [-1]
    for li in arr :
        if li == answer[-1] :
            continue
        else :
            answer.append(li)
    answer.pop(0)
    return answer
