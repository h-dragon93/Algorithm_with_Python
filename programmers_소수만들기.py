from itertools import combinations

def is_prime_number(x):    
    for i in range(2, x):
        if x % i == 0:
            return False 
    return True 

def solution(nums):
    result =0
    combination_3 = combinations(nums,3)    
    combiList = list(combination_3)
    for i in combiList :
        if(is_prime_number(sum(i))) :
            result += 1
    return result
