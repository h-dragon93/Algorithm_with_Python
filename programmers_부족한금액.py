def solution(price, money, count):
    
    tmpList = [ i * price for i in range(1, count+1) ] 
    
    if sum(tmpList) <= money :
        return 0
    else :
        return sum(tmpList) - money
