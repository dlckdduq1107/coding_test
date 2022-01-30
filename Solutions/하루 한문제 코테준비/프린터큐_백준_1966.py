from collections import deque
n = int(input())

for i in range(n):
    total,target = map(int,input().split())
    important = deque([])
    temp = list(map(int,input().split()))
    max_num = max(temp)
    for idx,j in enumerate(temp):
        important.append((j,idx))

    count = 1
    while(important):
        max_num = max([i[0] for i in important])
        value,idx = important[0]
        if(value>=max_num):
            v,ii = important.popleft()
            if(ii==target):
                print(count)
                break
            count += 1
        else:
            important.append(important.popleft())
