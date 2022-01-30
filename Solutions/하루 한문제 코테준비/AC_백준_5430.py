from collections import deque
n = int(input())

for i in range(n):
    func = input()
    length = int(input())
    arr = deque(eval(input()))
    flag = False
    rever = False
    for j in func:
        if(j=='R'):
            rever = not rever
        elif(j=='D'):
            if(arr):
                if(rever):
                    arr.pop()
                else:
                    arr.popleft()
            else:
                print('error')
                flag = True
                break
    if(not flag):
        if(rever):
            arr.reverse()
        print('['+','.join(list(map(str,arr)))+']')