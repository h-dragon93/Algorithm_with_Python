def solution(s) :
    pc = []
    for i in range(0, len(s)) :
        for j in range(1, len(s) + 1) :
            if s[i:j] == s[i:j][::-1] :
                pc.append(len(s[i:j]))
    return max(pc)
