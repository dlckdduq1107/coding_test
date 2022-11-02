


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
    
def switchFirst(isClick,current_state,target_state):
    result = 0
    for i in range(n):
        if(i==0):
            if(isClick):
                change(i,current_state)
                result += 1
        else:
            if(current_state[i-1]!=target_state[i-1]):
                change(i,current_state)
                result += 1
        
    if(current_state == target_state):
        return result
    else:
        return -1
n = int(input())
current_state = list(map(int,list(input())))
current_state = [False if i==0 else True for i in current_state]
target_state = list(map(int,list(input())))
target_state = [False if i==0 else True for i in target_state]

res1 = switchFirst(True, deepcopy(current_state), target_state)
res2 = switchFirst(False, deepcopy(current_state), target_state)

if(res1>=0 and res2>=0):
    print(min(res1,res2))
elif(res1==-1 and res2==-1):
    print(-1)
elif(res1==-1 or res2==-1):
    print(max(res1,res2))

