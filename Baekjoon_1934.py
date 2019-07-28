count = int(input())

for i in range(count) :
    a , b = input().split()
    a = int(a)
    b = int(b)

    xy = a
    xz = b

    while b != 0 :
        r = a%b
        a = b
        b = r

    gcd = a

    x = int(xy/gcd)
    y = int(xz/gcd)

    print(x*y*gcd)
