from itertools import combinations

def solution(nums):
    
    cnt = int(len(nums) / 2)  # 고를 수 있는 가지 수
    
    nums = list(set(nums))    # 중복 제거 포켓몬 수
    
    maxCnt = cnt
    
    if  cnt  >=  len(nums) :
        maxCnt = len(nums)

    return maxCnt
