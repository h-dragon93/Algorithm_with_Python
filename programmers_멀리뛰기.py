def solution(num):
    s1, s2 = 1, 2
    for i in range(num - 1):
        s1, s2 = s2, s1 + s2
    return s1 % 1234567
