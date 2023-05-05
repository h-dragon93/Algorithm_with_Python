from itertools import product

def solution(word):
    moum = ['A', 'E', 'I', 'O', 'U']
    ans = []
    for i in range(1,6) :
        for prod in product(moum, repeat = i) :
            ans.append(''.join(prod))
    ans.sort()
            
    
    return ans.index(word)+1
