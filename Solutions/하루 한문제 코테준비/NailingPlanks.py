def solution(A, B, C):
    res = []
    result = 0
    for i in range(len(A)):
        res.append([i for i in range(A[i],B[i]+1)])
    flag = [0 for i in range(len(A))]
    for idx,i in enumerate(C):
        if(sum(flag)==len(A)):
            result = idx
            break
        for j in range(len(res)):
            if(flag[j]):
                continue
            if(i in res[j]):
                flag[j] = 1
    return result