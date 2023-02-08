def solution(elements):
    
    length = len(elements)
    elements.extend(elements)
    unique = set()
    
    for i in range( length) :
        for j in range( length) :
            unique.add(sum(elements[j:j+i+1]))
    return len(unique)
