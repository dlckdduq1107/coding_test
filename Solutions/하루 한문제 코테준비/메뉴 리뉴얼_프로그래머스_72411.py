from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    result = []
    for i in orders:
        temp = sorted(i)
        for j in course:
            t = list(combinations(temp,j))
            result.extend(t)
            #print(t)
    #print(result)
    res = Counter(result)
    count = {}
    #print(res)
    for i in res:
        if(res[i] >=2 and len(i) not in count):
            #answer.append("".join(i))
            count[len(i)] = [(res[i],"".join(i))]
            #print(len(i),res[i])
        elif(res[i]<2):
            pass
        elif(res[i] >= count[len(i)][0][0]):
            if(res[i]==count[len(i)][0][0]):
                count[len(i)].append((res[i],"".join(i)))
            else:
                count[len(i)] = [(res[i],"".join(i))]
    #print(count)
    for i in count:
        for j in count[i]:
            answer.append(j[1])



    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))