def solve(K, N, M, station_list) :
    start = 0; count = 0; ans = 0; last_station = 0
    road = [0] * (N+1)
    for i in range(len(station_list)) :                            # 주유소가 있는 정류장과 없는 정류장을 0,1로 구분한 리스트
        tmp_num = station_list.pop(0)
        road[tmp_num] = 1
    while count < N :
        start += 1
        count += 1
        if count == N :                                            # 무사히 정류장에 도달했으면
            return ans
        if start == K :
            tmp_list = road[:count+1]
            station = len(tmp_list) - 1 - tmp_list[::-1].index(1)
            if last_station == station :                           # 기름이 모자라 정류장에 도달할 수 없으면
                return 0
            last_station = station
            start = 0
            count = station                                        # 충전한 위치에서 재시작
            ans += 1

T = int(input())
for test_case in range(1, T+1) :
    input_list = list(map(int, input().split()))
    K = input_list[0] ; N = input_list[1] ; M = input_list[2]
    station_list = list(map(int, input().split()))
    print('#{0} {1}'.format(test_case, solve(K, N, M, station_list)))
