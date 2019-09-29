import sys
sys.stdin = open("sample_input.txt", "r")             # 자동 입력

def make_graph(tmp_li) :                              # dfs를 위한 그래프
    tmp_dict = dict()
    for i in range(len(tmp_li)//2) :
        a = tmp_li.pop(0)
        b = tmp_li.pop(0)
        if a not in tmp_dict :
            tmp_dict[a] = [b]
        else :
            tmp_dict[a] += [b]
    return tmp_dict

def dfs(graph, start_node) :                         # dfs
    visit = list()
    stack = list()
    stack.append(start_node)
    while stack :
        node = stack.pop()
        if node not in visit :
            visit.append(node)
            if node in graph :
                stack.extend(graph[node])
            else :
                continue
    return visit

T = int(input())                                   # 프로그램 시작
for test_case in range(1, T + 1):
    E, N = map(int, input().split())                # E = 간선 개수, N = 서브 노드의 루트
    tmp_li = list(map(int, input().split()))
    root = tmp_li[0]
    graph_made = make_graph(tmp_li)
    check = dfs(graph_made, N)
    print('#{0} {1}'.format(test_case, len(check)))
