def bfs_paths(graph, start, goal) :
    result = []
    queue = [(start, [start])]
    while queue :
        n, path = queue.pop(0)
        if n == goal:
            result.append(path)
            return result
        else:
            for m in graph[n] - set(path):
                queue.append((m, path + [m]))
    # 연결된 간선이 없는 노드가 start일 경우
    return [[0]]

def make_graph(edge) :
    graph = dict()
    for i in range(len(edge)):
        if edge[i][0] not in graph:
            graph[edge[i][0]] = [edge[i][1]]
        elif edge[i][1] not in graph[edge[i][0]]:
            graph[edge[i][0]].append(edge[i][1])

        if edge[i][1] not in graph:
            graph[edge[i][1]] = [edge[i][0]]
        elif edge[i][0] not in graph[edge[i][1]]:
            graph[edge[i][1]].append(edge[i][0])
    for i in graph:
        graph[i] = set(graph[i])

    return graph

def solution(edge, start, goal) :
    graph = make_graph(edge)
    path = bfs_paths(graph, start, goal)

    return len(path[0]) - 1

T = int(input())
for test_case in range(1, T+1) :
    V, E = map(int, input().split())  # 노드의 개수 : V, 간선 개수 : E
    edge = [ list(map(int, input().split())) for _ in range(E) ]
    start, goal = map(int, input().split())
    print('#{0} {1}'.format(test_case, solution(edge, start, goal)))
