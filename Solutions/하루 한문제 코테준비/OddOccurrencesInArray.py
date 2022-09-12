def solution(A):
    result = 0
    res_dict = defaultdict(bool)
    for i in A:
        res_dict[i] = not res_dict[i]
    for i in res_dict:
        if(res_dict[i]):
            result = i

    return result