def solve(arr) :
    count = 0
    for i in range(2, len(arr) -2) :
        height = arr[i]
        left = max(arr[i-2:i])
        if height < left :
            continue
        right = max(arr[i+1:i+3])
        if height < right :
            continue
        possible_height = max(left, right)
        count += (height - possible_height)
    return count

if __name__ == "__main__" :
    for i in range(10) :
        t = int(input())
        array = list(map(int, input().split()))
        print("#{0} {1}".format(i+1, solve(array)))
