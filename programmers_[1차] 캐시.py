from collections import deque

def checkInCache(cache, city) :
    if city in cache :
        return True
    else :
        return False

def solution(cacheSize, cities):
    
    cache = deque()
    time = 0

    for city in cities :
        city = city.lower()
        if len(cache) < cacheSize :
            if(checkInCache(cache, city)) :
                cache.remove(city)
                cache.append(city)
                time += 1
            else :
                cache.append(city)
                time += 5

        else :
            if city in cache :
                cache.remove(city)
                cache.append(city)
                time += 1
            else :
                if cache :
                    cache.popleft()
                    cache.append(city)
                time += 5
    
    return time
