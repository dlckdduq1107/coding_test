def solution(queue1, queue2):
    answer = 0
    while(sum(queue1)!=sum(queue2)):
        if(sum(queue1)>sum(queue2)):
            pop_each = queue1.pop(0)
            queue2.append(pop_each)
        else:
            pop_each = queue2.pop(0)
            queue1.append(pop_each)
        answer += 1
        if(answer > len(queue1)*2):
            answer = -1
            break

    return answer

print(solution([3, 2, 7, 2],[4, 6, 5, 1]))