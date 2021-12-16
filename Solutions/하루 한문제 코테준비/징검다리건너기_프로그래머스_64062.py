def solution(stones, k):
    answer = 0
    start,end = 1,max(stones)

    while start<=end:
        mid = (start+end)//2
        blank = 0
        for each in stones:
            if(each-mid<=0):
                blank += 1
            else:
                blank = 0
            if(blank>=k):
                break

        if(blank<k):
            start = mid + 1
        else:
            answer = mid
            end = mid-1

    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))