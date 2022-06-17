from collections import defaultdict
import copy
def solution(N, stages):
    answer = []
    result = defaultdict(float)
    temp = sorted(stages)
    total = len(stages)
    for i in range(1,N+1):
        t = 0
        for j in stages:
            if(i==j):
                t += 1
        result[i] = t/total if total!=0 else 0 # total이 이미 소진되었을때 0이 되기 때문에 0으로 나눌수 없는 에러가 발생한다.
        total -= t
    for i in result:
        answer.append([i,result[i]])
    answer.sort(key=lambda x:x[0])
    answer.sort(key=lambda x:x[1], reverse=True)
    a = [i[0] for i in answer]
    return a