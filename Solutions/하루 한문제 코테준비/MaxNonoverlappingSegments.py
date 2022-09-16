def solution(A, B):
    tasks = []
    for i in range(len(A)):
        tasks.append([A[i],B[i]])
    tasks.sort(key=lambda x:x[1])
    result = 0
    until = -1
    for start,end in tasks:
        if(until<start):
            result += 1
            until = end
    return result
