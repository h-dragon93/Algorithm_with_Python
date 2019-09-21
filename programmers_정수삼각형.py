def solution(triangle):
    ans = []
    for row in triangle:
        lst = []
        if len(ans) == 0:
            lst.append(row[0]);
        else:
            for idx, num in enumerate(row):
                if idx == 0:
                    lst.append(ans[-1][idx] + num)
                elif idx == len(row)-1:
                    lst.append(ans[-1][-1] + num)
                else:
                    lst.append(max(ans[-1][idx-1],ans[-1][idx]) + num)
        ans.append(lst)
    return max(ans[-1])
