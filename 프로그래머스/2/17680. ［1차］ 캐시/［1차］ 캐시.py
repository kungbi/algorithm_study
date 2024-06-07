

def caching(caches, cacheSize, city, t):
    found = False
    min_time = float('inf')
    for i in range(len(caches)):
        if caches[i][0] == city:
            caches[i][1] = t
            found = True
        min_time = min(min_time, caches[i][1])
    
    if found == True:
        return True
    
    if len(caches) < cacheSize:
        caches.append([city, t])
        return False
    
    
    for i in range(len(caches)):
        if caches[i][1] == min_time:
            caches[i] = [city, t]
            break
    return False
    
    

def solution(cacheSize, cities):
    caches = []
    
    time = 0
    for i in range(len(cities)):
        if caching(caches, cacheSize, cities[i].lower(), i):
            time += 1
        else:
            time += 5
    return time
        
        