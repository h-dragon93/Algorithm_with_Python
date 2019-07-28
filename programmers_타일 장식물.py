def solution(N):
    sero = [1]*N
    garo = [1]*N
    for i in range(N-1) :
        if i % 2 == 0 :
            sero[i+1] = sero[i] + garo[i]
            garo[i+1] = garo[i]
        else :
            sero[i+1] = sero[i]
            garo[i+1] = sero[i] + garo[i]

    answer = sero[N-1]*2 + garo[N-1]*2
    return answer
