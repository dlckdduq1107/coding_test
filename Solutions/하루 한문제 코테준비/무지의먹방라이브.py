import heapq
def solution(food_times, k):
    answer = -1
    q =[]
    for i in range(len(food_times)):
        heapq.heappush(q,[food_times[i], i+1])

    remain_food = len(food_times)
    previous = 0
    while q:
        time = (q[0][0]-previous)*remain_food
        if(k>=time):
            k -= time
            previous,_ = heapq.heappop(q)
            remain_food -= 1
        else:
            idx = k%remain_food
            q.sort(key=lambda x:x[1])
            answer = q[idx][1]
            break
    return answer



    
print(solution([3, 1, 2], 5))