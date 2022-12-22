
from collections import defaultdict
from itertools import combinations

def solution(relation):
    answer = 0
    attr_count = len(relation[0])
    data_count = len(relation)
   
    candidates = []
    for i in range(1,attr_count+1):
        candidates.extend(combinations(range(attr_count),i))
    # print(candidates)

    unique = []
    for i in candidates:
        temp = [tuple(item[j] for j in i)  for item in relation]
        # print(temp)
        if(len(set(temp)) == data_count):
            unique.append(i)
    # print(unique)

    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if(len(unique[i])==len(set(unique[i])&set(unique[j]))):
                answer.discard(unique[j])
    return len(answer)
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))