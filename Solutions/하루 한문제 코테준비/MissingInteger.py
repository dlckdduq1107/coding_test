import copy
def solution(A):
    result = 1
    cpy_A = list(set(copy.deepcopy(A)))
    cpy_A.sort()

    for idx,i in enumerate(cpy_A):
        if(i==result):
            result += 1

    return result