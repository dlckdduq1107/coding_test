from collections import deque

n,Q,total = map(int,input().split(" "))
capacity = 0
cache = [0]+ list(map(int,input().split(" ")))
back = deque([])
front = deque([])
current = 0

for i in range(Q):
    each = list(map(str,input().split(" ")))
    direct = each[0]
    if(direct == "B"):
        if(len(back)>0):
            front.appendleft(current)
            current = back.pop()
    elif(direct == "F"):
        if(len(front)>0):
            back.append(current)
            current = front.popleft()
    elif(direct == "A"):
        for i in front:
            capacity -= cache[i]
        front.clear()
        if(current != 0):
            back.append(current)

        current = int(each[1])
        capacity += cache[current]
        temp = capacity
        if(temp > total):
            while temp > total:
                temp -= cache[back.popleft()]
            capacity = temp

    elif(direct == "C"):
        t = []
        minus = 0
        for i in back:
            if( i in t and pre==i):
                minus += cache[i]
            else:
                t.append(i)
            pre = i
        back.clear()
        for i in t:
            back.append(i)
        capacity -= minus


print(current)
if(len(back)==0):
    print(-1)
else:
    for i in range(len(back)-1,-1,-1):
        if(i==0):
            print(back[i])
        else:
            print(back[i],end=" ")

if(len(front)==0):
    print(-1)
else:
    for idx,i in enumerate(front):
        if(idx==len(front)-1):
            print(i)
        else:
            print(i,end=" ")