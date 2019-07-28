n = int(input()) # 총 몇층인지
li = [0]*(n+1) # 각층의 값
f = [0]*(n+1) # 각층에 도착시의 최대 합을 저장할 list
for i in range(1,n+1):
    li[i] = int(input())
f[1] = li[1] # 1층의값
if n>=2:
    f[2] = li[1] + li[2]
if n>=3:
    f[3] = (li[1] if li[1] >= li[2] else li[2]) + li[3]

for n in range(4, n+1):
    f[n] = max(f[n-2] + li[n], f[n-3] + li[n-1] + li[n])
print(f[n])
