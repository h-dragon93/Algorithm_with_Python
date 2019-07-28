n=int(input())
num = []
num.append(list(map(int,input().split())))
lastsum = []
totalsum = [num[0][0]]
 
for i in range(1,n):
    num.append(list(map(int,input().split())))
    lastsum = totalsum
    totalsum =[]
    for j in range(0,i+1):
        if j == 0:
            totalsum.append(lastsum[0] + num[i][0]) # 가장 왼쪽
        elif j < i and j > 0:
            totalsum.append(num[i][j]+ max(lastsum[j-1],lastsum[j])) # 내부
        else:
            totalsum.append(lastsum[i-1] + num[i][j]) # 가장 오른쪽
 
print(max(totalsum))
