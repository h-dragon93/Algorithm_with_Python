def solution(lottos, win_nums):
    
    #1 일치하는 번호 개수 인덱스에 대응되는 순위가 위치한 순위 리스트
    rankList = [6, 6, 5, 4, 3, 2, 1]
    
    #2 일치하는 번호 개수 구하기
    cnt = 0
    
    for i in lottos : # 구매 번호가 당첨 번호에 있다면 cnt +1
        if i in win_nums : cnt += 1 
    
    #3 최고 순위, 최저 순위 구하기
    rankHigh = rankList[cnt + lottos.count(0)]
    rankLow = rankList[cnt]
    
    answer = [rankHigh, rankLow]

    return answer
  
  
  
  
#출처 : https://stackstackstack.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A1%9C%EB%98%90%EC%9D%98-%EC%B5%9C%EA%B3%A0-%EC%88%9C%EC%9C%84%EA%B3%BC-%EC%B5%9C%EC%A0%80-%EC%88%9C%EC%9C%84-%ED%8C%8C%EC%9D%B4%EC%8D%AC
