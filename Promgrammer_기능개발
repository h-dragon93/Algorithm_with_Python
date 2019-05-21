def solution(progresses, speeds):
    li = []
    li_count = []
    for i in range(len(progresses)):
        li.append(progresses[i])
        count = 0
        while li[i] < 100:
            li[i] = li[i] + speeds[i]
            count += 1
        li_count.append(count)
        answer = []

    print(li_count)
    count = 1
    cur = li_count.pop(0)
    while len(li_count) != 0 :
        if li_count[0] <= cur :
            li_count.pop(0)
            count += 1
        else :
            answer.append(count)
            count = 1
            cur = li_count.pop(0)
    answer.append(count)

    return answer
