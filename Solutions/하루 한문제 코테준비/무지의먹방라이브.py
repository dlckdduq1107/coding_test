import copy
def solution(food_times, k):
    answer = 0
    temp = copy.deepcopy(food_times)
    pivot = 0
    time = 0
    while time!=k:
        if(pivot>=len(temp)):
            pivot = 0
        if(temp[pivot]>0):
            temp[pivot] -= 1
            pivot += 1
        else:
            if(sum(temp)==0):
                return -1
            while temp[pivot]==0:
                pivot += 1
            temp[pivot] -= 1
        time += 1
        print(temp)
    return (pivot+1)%len(temp)+1
print(solution([3, 1, 2], 5))