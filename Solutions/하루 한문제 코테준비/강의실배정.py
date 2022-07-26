import heapq
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split(" "))))
end_time = []
graph.sort(key=lambda x:x[0])
result = 0
heapq.heappush(end_time,graph.pop(0)[1])
for s,e in graph:
    if(end_time[0]>s):
        heapq.heappush(end_time,e)
    else:
        heapq.heappop(end_time)
        heapq.heappush(end_time,e)
print(len(end_time))