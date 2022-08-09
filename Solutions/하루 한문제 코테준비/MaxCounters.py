def solution(N, A):
    counter = [0 for i in range(N)]
    max_value = 0
    save = 0
    for i in A:
        if(N+1==i):
            save = max_value
        else:
            if(counter[i-1]<save):
                counter[i-1] = save
            counter[i-1] += 1
            max_value = max(counter[i-1],max_value)
    for idx,i in enumerate(counter):
        if(i<save):
            counter[idx] = save
    return counter