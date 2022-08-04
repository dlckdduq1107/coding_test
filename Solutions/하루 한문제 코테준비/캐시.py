def solution(cacheSize, cities):
    answer = 0
    cache = []
    for i in cities:
        i = i.upper()
        if(cacheSize==0):
            answer += 5
            continue
        if(i in cache):#hit
            cache.remove(i)
            cache.append(i)
            answer += 1
        else:#miss
            # if(cache != []):
            #     cache.pop(0)
            if(len(cache)==cacheSize):
                cache.pop(0)
            cache.append(i)
            answer += 5
        # print(cache)
    return answer
print(solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))