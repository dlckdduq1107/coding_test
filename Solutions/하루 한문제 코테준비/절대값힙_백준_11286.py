import heapq
import sys

n = int(sys.stdin.readline())

q = []
for i in range(n):
    num = int(sys.stdin.readline())
    if(num==0):
        if(q):
            res,number = heapq.heappop(q)
            print(number)
        else:
            print(0)
    else:
        heapq.heappush(q,(abs(num),num))