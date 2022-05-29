import sys
from collections import deque

N = int(sys.stdin.readline())

carList= deque([i+1 for i in range(N)])

while len(carList) != 1 :
    carList.popleft()
    if len(carList) == 1 :
        break
    carList.rotate(-1)

print(carList[0])

# 리스트 맨앞, 맨뒤만 필요할때는 List 대신 deque 사용 O(N) -> O(1)
# 원형 큐에 쓰기 좋은 rotate 메소드
# 이 문제 반례는 1 주어진 숫자 1 일때 생각해보면 됨..
