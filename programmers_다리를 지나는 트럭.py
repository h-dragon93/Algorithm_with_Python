def solution(bridge_length, weight, truck_weights):
    bridge = [0]*(bridge_length)
    answer = 0

    while bridge :
        print(bridge)

        bridge.pop(0)
        answer += 1
        if truck_weights :

            if sum(bridge) + truck_weights[0] > weight :
                bridge.append(0)
                continue

            else :
                bridge.append(truck_weights.pop(0))

    return answer
