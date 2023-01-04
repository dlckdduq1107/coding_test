from audioop import maxpp
from itertools import combinations
from collections import Counter, defaultdict

def solution(orders, course):
    answer = []
    combi = defaultdict(int)
    for i in range(len(orders)):
        for j in range(2,len(orders[i])+1):
            for each in combinations(orders[i],j):
                combi[''.join(sorted(list(each)))] += 1
    # print(combi)
    max_dict = {}
    for i in course:
        max_dict[i] = [[],0]
    # print(max_dict)
    for i in combi:
        # print(len(i) in max_dict, i)
        if(combi[i]>1 and len(i) in course and len(i) in max_dict.keys()):
            if(max_dict[len(i)][1]<combi[i]):
                max_dict[len(i)]= [[i],combi[i]]
            elif(max_dict[len(i)][1]==combi[i]):
                max_dict[len(i)][0].append(i)
            else:
                pass
    # print(max_dict)
    for i in max_dict:
        answer.extend(max_dict[i][0])
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))