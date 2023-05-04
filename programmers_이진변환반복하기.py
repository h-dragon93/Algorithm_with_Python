def solution(s):
    eleminated = 0
    converted = 0
    while True:
        originStrLength = len(s)
        s = s.replace("0", "")
        replacedStrLength = len(s)
        eleminated += (originStrLength - replacedStrLength)
        s = format(len(s), 'b')
        converted += 1

        if s == "1":
            return [converted, eleminated]
        
