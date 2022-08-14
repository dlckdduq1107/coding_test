def solution(A):
    min_value = A[0] if len(A)!=0 else 0
    result = 0
    for i in A:
        if(i<min_value):
            min_value = i
        else:
            result = max(i-min_value,result)

    return result