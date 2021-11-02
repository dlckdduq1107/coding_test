import sys
from collections import deque

input = sys.stdin.readline
n,time = map(int,input().split(" "))
maxEnd = -1
total = deque([])
total.extend([0 for i in range(100000)])
w = deque([])
for i in range(n):
    e = int(input())
    for j in range(e):
        s,e = map(int,input().split(" "))
        w.append((s,e))
        # for q in range(s,e):
        #     total[q] += 1
        maxEnd = max(maxEnd,e)
for ss,ee in w:
    for i in range(ss,ee):
        total[i] += 1

sum_value = 0
prefix = deque([0])
for i in range(maxEnd):
    sum_value += total[i]
    prefix.append(sum_value)

# print(total)
# print(prefix)
maxResult = -1
rx,re = 0,0
for i in range(maxEnd-time):
    a,b = i,i+time
    temp = prefix[b]-prefix[a]
    if(temp>maxResult):
        maxResult = temp
        rx,re = a,b

print(rx,re)