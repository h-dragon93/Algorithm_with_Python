def solve(N, M, li) :
    tmp_max = 0; tmp_min = 10000*M
    for i in range(N-(M-1)) :
        tmp_sum = 0
        for j in range(M) :
            tmp_sum += li[i+j]
        if tmp_max < tmp_sum :
            tmp_max = tmp_sum
        if tmp_min > tmp_sum :
            tmp_min = tmp_sum
    return tmp_max-tmp_min

T = int(input())
for test_case in range(1, T+1) :
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    print('#{0} {1}'.format(test_case, solve(N, M, li)))
