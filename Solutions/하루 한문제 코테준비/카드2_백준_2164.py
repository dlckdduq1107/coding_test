from collections import deque
n = int(input())

q = deque([i for i in range(n,0,-1)])
# print(q)
if(n<3):
    print(n)
else:
    while(len(q)>1):
        q.pop()
        q.appendleft(q.pop())
        # print(q)
    print(q[0])
