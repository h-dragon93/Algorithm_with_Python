import itertools

def makeDict(clothes) :
    clothesDict = dict()
    for name, type in clothes :
        if type not in clothesDict :
            clothesDict[type] = [name]
        else :
            tmpList = clothesDict[type]
            tmpList.append(name)
            clothesDict[type] = tmpList
    return clothesDict


def solution(clothes):
    ans = 1
    clothesDict = makeDict(clothes)
    for value in clothesDict.values() :
        ans *= len(value) + 1
    print(ans)

    return ans-1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    solution(clothes)



