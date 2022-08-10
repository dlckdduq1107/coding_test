def solution(N, A):
    counter = [0 for i in range(N)]
    # max_value = -int(1e9)
    for i in A:
        if(N+1==i):
            counter = [max(counter) for i in range(N)]
        else:
            counter[i-1] += 1
    return counter