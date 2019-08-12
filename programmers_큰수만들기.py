def solution(number, k):
    length = len(number)
    if length > k:
        start = 0
        for cnt in range(k):
            for idx in range(start, length-1):
                if number[idx] < number[idx+1]:
                    number = number[:idx] + number[idx+1: ]
                    length -= 1
                    if idx > 0:
                        start = idx-1
                    break
            else:
                number = number[:length-k+cnt]
                break
        return "".join([str(i) for i in number])
    else:
        return "0"
