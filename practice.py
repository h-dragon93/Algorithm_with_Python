def solution(goods, boxes):
    goods = sorted(goods)
    boxes = sorted(boxes)
    li = []
    k = 0
    for i in range(len(goods)) :
        for j in range(k, len(boxes)) :
            if goods[i] <= boxes[j] :
                li.append(goods[i])
                k = j+1
                break

    return len(li)
