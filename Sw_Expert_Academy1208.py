def solve(dump_count, boxes) :
    for i in range(dump_count) :
        max_index = boxes.index(max(boxes))
        min_index = boxes.index(min(boxes))
        boxes[max_index] -= 1
        boxes[min_index] += 1
        if max(boxes) - min(boxes) <= 1 :
            break
    return max(boxes) - min(boxes)

if __name__ == "__main__" :
    for i in range(1, 11) :
        dump_count = int(input())
        boxes = list(map(int, input().split()))
        print('#{0} {1}'.format(i, solve(dump_count, boxes)))
