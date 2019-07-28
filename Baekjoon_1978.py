count = int(input())
li = []
li = list(map(int,input().split()))
count = 0
def is_prime (li) :
    if li == 1 :
        return False
    else :
        for i in range(2, li) :
            if li % i == 0 :
                return False
    return True

for i in range(len(li)) :
    if is_prime(li[i]) == True :
        count += 1
print(count)
