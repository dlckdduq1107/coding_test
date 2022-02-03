import heapq
import sys
n = int(sys.stdin.readline())
q = []
for i in range(n):
    num = int(sys.stdin.readline())
    if(num==0):
        if(q):
            print(-heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q,-num)