def compareDiff(origin, compare) :
    cnt = 0
    if len(origin) != len(compare) :
        origin = "0"+origin
    for i in range(len(origin)) :
        if origin[i] != compare[i] :
            cnt += 1
    return cnt

def getBiggerBit(num):
    origin = format(num, 'b')
    while True:
        num += 1
        compare = format(num, 'b')
        tmp = compareDiff(origin, compare)
        if tmp == 1 or tmp == 2 :
            return num


def solution(numbers):
    answer = []
    for num in numbers:
        ans = getBiggerBit(num)
        answer.append(ans)

    return answer
