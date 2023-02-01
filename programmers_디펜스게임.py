import heapq
def solution(n, k, enemy):
    heap = []
    # if len(enemy) == k:       # 없어도 돌아가지만 최적화
    #     return len(enemy)
    for i in range(len(enemy)):
        if n >= enemy[i]:       # 아군이 적군보다 같거나 많으면
            heapq.heappush(heap, -enemy[i])  # 현재 상대한 적군은 일단 최대힙에 담고
            n -= enemy[i]                    # 아군은 일단 죽은걸로 한다
        else:                   # 아군이 적군보다 적으면
            if k > 0:                        # 무적권이 있고
                if heap:                            # 최대힙에 담아둔 아군이 있다면
                    a = -heapq.heappop(heap)        # 아군을 꺼내서
                    k -= 1                          # 무적권을 과거에 사용한 것처럼 바꿔치기
                    if a >= enemy[i]:                   # 최대힙에서 꺼낸 아군이 적군보다 같거나 크다면
                        n = n + (a - enemy[i])               # 적을 상대하고 남은 아군을 현재 아군에 더하고
                        heapq.heappush(heap, -enemy[i])      # 최대힙에 상대한 적군을 넣어준다(다음턴에는 이녀석이 최대값이 될 수도 있다)
                    else:                               # 최대힙에서 꺼낸 아군이 적군보다 작다면
                        heapq.heappush(heap, -a)             # n(아군)은 사용하지 않고 무적권만 사용한것으로 한다. 무적권을 썼으므로, 꺼낸 아군은 다시 담아둔다
                else:
                    k -= 1       
            else:               # 아군이 적군보다 적고 무적권도 없다면 게임 끝
                return 
