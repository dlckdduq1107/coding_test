import heapq
import sys
q = []

n = int(input())
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if q == []:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q,x)