import copy
def solution(A, K):
    result = copy.deepcopy(A)
    if(result != []):
        for i in range(K):
            pop_item = result.pop()
            result = [pop_item]+result
    return result