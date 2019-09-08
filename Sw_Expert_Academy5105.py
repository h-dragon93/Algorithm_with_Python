import sys
sys.stdin = open("sample_input.txt", "r")

def IsSafe(x,y ):
    return 0<= x < N and 0 <= y < N  and (Maze[x][y] == 0 or Maze[x][y] == 3)

def bfs(start_x, start_y) :
    global D_result
    queue = []
    visited = [[0] * N for _ in range(N)]
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    Distance = [[0] * N for _ in range(N)]
    queue.append((start_x, start_y))
    visited.append((start_x, start_y))
    while queue :
        start_x, start_y = queue.pop(0)
        for direction in range(4):
            NewX = start_x + dx[direction]
            NewY = start_y + dy[direction]
            if IsSafe(NewX, NewY) and (NewX, NewY) not in visited :
                queue.append((NewX, NewY))
                visited.append((NewX, NewY))
                Distance[NewX][NewY] = Distance[start_x][start_y] +1
                if Maze[NewX][NewY] == 3:
                    D_result = Distance[NewX][NewY] -1
                    return

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    Maze = [list(map(int, input())) for _ in range(N)]
    for x in range (N) :
        for y in range(N) :
            if Maze[x][y] == 2 :
                start_x, start_y = x, y
    D_result = 0
    bfs(start_x, start_y)
    print('#{0} {1}'.format(test_case, D_result))
