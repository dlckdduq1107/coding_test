from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    answer = []
    res = {}
    for i in info:
        each = i.split(" ")
        tk = each[:-1]
        tv = each[-1]
        for j in range(5):
            for p in combinations(tk,j):
                temp = "".join(p)
                if temp in res:
                    res[temp].append(int(tv))
                else:
                    res[temp] = [int(tv)]
    for i in res:
        res[i].sort()

    for i in query:
        qu,ss = "".join(i.split(" and ")).replace("-","").split(" ")
        if(qu in res):
            if(res[qu]):
                tt = bisect_left(res[qu],int(ss))
                answer.append(len(res[qu])-tt)
        else:
            answer.append(0)



    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))