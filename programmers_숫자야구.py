from itertools import permutations

def tuple_to_str(tuple_):
    result = ""
    for number in tuple_:
        result += str(number)
    return result

def get_candidate(num) :
    numbers = list(range(1, 10))
    candidates = list(permutations(numbers, num))
    return candidates

def validation(guess, candidate) :
    target_num, target_strike, target_ball = guess
    target_num_str = str(target_num)
    candidate_str = tuple_to_str(candidate)
    strike = 0
    ball = 0
    is_correct = True

    for str1, str2 in zip(target_num_str, candidate_str) :
        if str1 == str2 :
            strike  += 1
        elif str1 in candidate_str :
            ball += 1
    if strike != target_strike or ball != target_ball :
        is_correct = False

    return is_correct

def check_candidate(baseball, candidate) :
    is_passed = True
    for guess in baseball:
        correct = validation(guess, candidate)
        if not correct:
            is_passed = False
            break
    return is_passed

def solution(baseball):
    candidates = get_candidate(3)
    count = 0
    for candidate in candidates :
        is_passed = check_candidate(baseball, candidate)
        if is_passed :
            count += 1
    return count
