from collections import deque
def topology():
    result = [] # 결과를 출력하기 위한 리스트
    q = deque()

    for i in range(1,v+1): # 전체 노드중에서 진입차수가 0인거 먼저 큐에 넣어줌
        if indegree[i] == 0:
            q.append(i)

    while q: # 큐가 빌때 까지
        now = q.popleft()
        result.append(now) # 결과 리스트에 넣어줌
        for i in graph[now]:  # 현재 노드에 연결된 노드들 탐색
            indegree[i] -= 1 # 연결된 노드의 진입차수 -=
            if indegree[i] == 0: # -1 한것의 진입차수가 0이 되면 큐에 넣어줌
                q.append(i)

    for i in result: # 결과 출력
        print(i,end=" ")


v,e = map(int,input().split(" "))
graph = [[] for i in range(v+1)] # 그래프
indegree = [0 for i in range(v+1)] # 진입차수 계산을 위한 리스트

for i in range(e): # 엣지 입력
    a,b = map(int, input().split(" "))
    graph[a].append(b) # 연결 상태 저장
    indegree[b] += 1 # 도착 지점의 진입차수 +=

topology()