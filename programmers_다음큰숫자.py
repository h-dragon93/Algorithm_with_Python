def solution(n):
    originOneCount = list(format(n, 'b')).count('1')
    
    while True :
        n += 1
        targetOneCount = list(format(n, 'b')).count('1')
        if targetOneCount == originOneCount :
            return 
