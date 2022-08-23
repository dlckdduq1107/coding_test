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
# 우선순위 큐를 이용해서 가장 빨리 끝나는 시간이 앞에 놓이도록 유지해야 다음 강의 시작 시간에 맞춰 판단할 수 있다.