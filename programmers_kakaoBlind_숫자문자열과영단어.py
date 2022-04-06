def checkInteger(str) :
    intList = ["1","2","3","4","5","6","7","8","9","0"]
    if str in intList :
        return True
    else :
        return False

def solution(s):
    intMap = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"} 
    result = ""
    tmpStr = ""
    for str in s :
        if checkInteger(str) :
            result = result + str
            tmpStr = ""
        else :
            tmpStr = tmpStr + str
            if tmpStr in intMap :
                result = result + intMap[tmpStr]
                tmpStr = ""
    return int(result)
