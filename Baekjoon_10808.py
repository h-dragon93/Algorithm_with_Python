s = input()

list(s)
li = [0] * 26
for str in s :
    li[ord(str)-97] += 1
for i in range(len(li)) :
    print(li[i], end=" ")
