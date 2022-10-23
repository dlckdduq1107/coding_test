import copy
from collections import deque
def solution(queue1, queue2):
    answer = 1
    first,second = deque(copy.deepcopy(queue1)), deque(copy.deepcopy(queue2))

    if(sum(first) == sum(second)):
        return 0
    
    else:
        if(sum(first)>sum(second)):
            popper = first.popleft()
            second.append(popper)
        else:
            popper = second.popleft()
            first.append(popper)
    flag = True
    for i in range(len(queue1)*4):
        if(sum(first)>sum(second)):
            popper = first.popleft()
            second.append(popper)
        elif(sum(first)==sum(second)):
            flag = False
            break
        else:
            popper = second.popleft()
            first.append(popper)
        answer += 1
        
    
    if(flag):
        return -1
    return answer

print(solution([3, 2, 7, 2],[4, 6, 5, 1]))
print(solution([1, 2, 1, 2]	,[1, 10, 1, 2]	))
print(solution([1, 1]	,[1, 5]	))