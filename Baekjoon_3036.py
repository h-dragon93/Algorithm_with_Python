N = int(input())

li = list(map(int, input().split(" ")))

def gcd(a, b) :
    if b == 0 :
        return a
    return gcd(b, a%b)

for i in range(len(li)-1) :
    a = gcd(li[0],li[i+1])
    print("%d/%d"%(int(li[0]/a),int(li[i+1]/a)))
