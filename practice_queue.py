messageNum, consumerNum = map(int, input().split(" "))
li = []
for i in range(messageNum) :
    li.append(int(input()))
thread = []
for i in range(consumerNum) :
    thread.append([0])

def queue(thread, consumerNum) :
    count = 0
    while True :
        for i in range(consumerNum) :
            if len(li) != 0:
                if thread[i][0] == 0 :
                    thread[i][0] = li.pop(0)
        for i in range(consumerNum) :
            thread[i][0] -= 1
        count += 1
        if len(li) == 0 :
            for i in range(consumerNum) :
                if thread[i][0] != 0 :
                    continue
                elif max(sum(thread, [])) == 0 :
                    return count

print(queue(thread, consumerNum))
