a = [0] * 26
b = [0] * 26
count = 0
str1 = input()
str2 = input()
a_gram = list(str1)
b_gram = list(str2)
for i in range(0, len(a_gram)):
    a[ord(a_gram[i]) - 97] += 1
for i in range(0, len(b_gram)):
    b[ord(b_gram[i]) - 97] += 1
for i in range(0, 26):
    if a[i] != b[i]:
        count += abs(a[i] - b[i])
print(count)
