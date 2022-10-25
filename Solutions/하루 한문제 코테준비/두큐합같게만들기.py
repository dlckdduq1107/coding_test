import copy
from collections import deque
def solution(queue1, queue2):
    answer = 1
    first,second = deque(copy.deepcopy(queue1)), deque(copy.deepcopy(queue2))
    sum_first, sum_second = sum(first), sum(second)
    if(sum_first == sum_second):
        return 0
    
    else:
        if(sum_first>sum_second):
            popper = first.popleft()
            second.append(popper)
            sum_first -= popper
            sum_second += popper
        else:
            popper = second.popleft()
            first.append(popper)
            sum_second -= popper
            sum_first += popper
    flag = True
    for i in range(len(queue1)*4):
        if(sum_first>sum_second):
            popper = first.popleft()
            second.append(popper)
            sum_first -= popper
            sum_second += popper
        elif(sum_first==sum_second):
            flag = False
            break
        else:
            popper = second.popleft()
            first.append(popper)
            sum_second -= popper
            sum_first += popper
        answer += 1
        
    
    if(flag):
        return -1
    return answer

print(solution([3, 2, 7, 2],[4, 6, 5, 1]))
print(solution([1, 2, 1, 2]	,[1, 10, 1, 2]	))
print(solution([1, 1]	,[1, 5]	))