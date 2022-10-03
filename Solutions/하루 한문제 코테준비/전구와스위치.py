from copy import copy, deepcopy


def change(index,arr):
    if(index==0):
        arr[0] = not arr[0]
        arr[1] = not arr[1]
    elif(index==len(arr)-1):
        arr[index] = not arr[index]
        arr[index-1] = not arr[index-1]
    else:
        arr[index-1] = not arr[index-1]
        arr[index] = not arr[index]
        arr[index+1] = not arr[index+1]
    

n = int(input())
current_state = list(map(int,list(input())))
current_state = [False if i==0 else True for i in current_state]
target_state = list(map(int,list(input())))
target_state = [False if i==0 else True for i in target_state]

cpy_current = deepcopy(current_state)
idx = 0
result = 0
while(current_state != target_state ):
    if(current_state[idx] != target_state[idx]):
        change(idx,current_state)
        result += 1
    if(idx==n-1):
        idx = 0
    else:
        idx += 1
    if(result != 0 and current_state == cpy_current):
        break
    # print(current_state)
    # print(target_state)
if(current_state==target_state):
    print(result)
else:
    print(-1)