N = int(input())
seat = list(map(int, input().split(" ")))

def cal_max(seat):
    max = 0
    check = 0
    for idx, seat in enumerate(seat) :
        if seat == 1 :
            count = 0
        else :
            count += 1
            if count > max :
                max = count
                check = idx
    return max, check

max, check = cal_max(seat)
dist = (check-max + check)//2
if dist % 2 == 0 :
    print(dist//2)
elif dist % 2 != 0 :
    print((dist//2)+1)
