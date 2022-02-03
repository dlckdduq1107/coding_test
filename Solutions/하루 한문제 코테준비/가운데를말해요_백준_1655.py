import heapq
import sys

n = int(sys.stdin.readline())
left,right = [],[]
for i in range(n):
    num = int(sys.stdin.readline())
    if(len(left)==len(right)):
        heapq.heappush(left,(-num,num))
    else:
        heapq.heappush(right,(num,num))
    if(right and left[0][1]>right[0][1]):
        left_prior,left_value = heapq.heappop(left)
        right_prior,right_value = heapq.heappop(right)
        heapq.heappush(left,(-right_prior,right_value))
        heapq.heappush(right,(-left_prior,left_value))
    print(left[0][1])

