from collections import deque
def check(graph,start,weight,end): # 웨이트로 도착 가능 한지 체크하는 함수
    queue = deque()
    queue.append(start)
    visited = [] # 지나간 자리 기록하는 리스트

    while queue:
        v = queue.popleft()

        for i,j in graph[v]:
            if i not in visited and weight <= j: # 지나간 적이 없고 설정된 웨이트로 지나갈 수 있으면
                visited.append(i) # 지나갔다는 표시
                queue.append(i) # 다음 큐 삽입

    if end in visited: # 도착지가 지나간 기록에 있으면
        return True
    else: # 없으면
        return False

n,m = map(int,input().split(" "))

graph = [[]]
for i in range(n):
    graph.append([])

for i in range(m): # 그래프에 웨이트추가하여 튜플로 입력
    q,w,e = map(int,input().split(" "))
    graph[q].append((w,e))
    graph[w].append((q,e))


fac1,fac2 = map(int,input().split(" ")) # 시작과 도착지점

start = 1
end = 1000000000
result = 0

while start <= end: # 이분 탐색
    mid = (start+end)//2

    if check(graph, fac1,mid,fac2): # 웨이트로 도달 가능하면
        result = mid
        start = mid+1
    else:
        end = mid-1

print(result)