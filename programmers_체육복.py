import copy

def solution(n, lost, reserve):
    # 가능하면 앞번호 부터 빌려나가야 뒷번호 학생이 최대로 빌릴 수 있으므로 정렬
    lost.sort()
    reserve.sort()
    # 여분리스트 수정을 위해 원본 배열 보관
    reserve_copy = copy.deepcopy(reserve)
    # 여분이 있었지만 도난당해 여분이 없어진 학생을 여분 리스트에서 제거
    reserve = [i for i in reserve if i not in lost]
    # 여분이 있었지만 도난당해 여분이 없어진 학생을 도난 리스트에서 제거
    lost = [j for j in lost if j not in reserve_copy]
    # 여분이 있었지만 도난당한 학생을 reserve, lost 양쪽 리스트에서 제거, 체육복 한벌만 갖고 있는 학생수 저장 
    answer = n - len(lost)
    # 도난 당한 리스트를 돌며 여분을 가진 학생꺼를 가져올 수 있는지 확인
    for i in lost :
        if i - 1 in reserve :
            reserve.remove(i-1)
            answer += 1
        elif i + 1 in reserve :
            reserve.remove(i+1)
            answer += 1
        else :
             continue
    
    return answer
