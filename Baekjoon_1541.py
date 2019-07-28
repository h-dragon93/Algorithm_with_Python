string = input()
fm = string.split("-")
answer = 0
for i in range(len(fm)) :
    temp = fm[i].split("+")
    sum = 0
    for j in range(len(temp)) :
        sum += int(temp[j])
    if (i == 0 ):
        answer += sum
    else :
        answer -= sum
print(answer)
