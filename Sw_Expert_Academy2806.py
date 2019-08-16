def possible(row):
    for i in range(row):             # 이전 열들을 탐색하면서 유망한 노드인지 확인
        if col[i] == col[row]:       # 상위 노드에서 같은 행에 퀸이 있는지 여부
            return False
        if abs(i - row) == abs(col[i] - col[row]): # 대각선 검사
            return False                           # 상위 노드의 퀸과 현재 노드의 퀸의
    return True                                    # 가로 세로 거리가 같은지 검사

def dfs(depth):
    global N, ans
    if depth == N:                      # 현재 열이 체스판을 넘어 섰으면 정답
        ans += 1
    else:
        for i in range(N):
            col[depth] = i              # 현재 위치하고 있는 노드의 좌표를 저장(row:열, i:행)
            if possible(depth):         # 유망한 노드 검토
                dfs(depth + 1)          # 유망한 노드이면 -> 서브 트리 이동 (해당 노드의 하위 노드)
            else:                     # 유망한 노드가 아니면 -> 백트래킹 수행
                col[depth] = 0          # 해당 노드는 가지치기

T = int(input())
for test_case in range(1, T + 1):     # 첫번째 퀸의 시작점은 행을 기준. (i = 1) => (1, 1), (i = 2) => (1, 2), (i = 3) => (1, 3)
    N = int(input())
    ans = 0
    for i in range(N) :
        col = [0] * N
        col[0] = i                     # col 배열의 인덱스는 열 , i 는 행
        print("first col", col)
        dfs(1)                         # DFS 수행 (다음 열인 1열 이동)
    print('#{} {}'.format(test_case, ans))
