import heapq
# 힙을사용하면 최소힙으로 정렬된다. 그래서 k시간이전에 다 먹어 버리는 경우는 음식을 빼주고 시간도 빼준다.
# 해당 음식을 다 먹는 시간이 k를 넘어가면 뒤에 남아있는 것은 모두 시간이 남는 것 이므로 그 중에서 순서를 구해준다.
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