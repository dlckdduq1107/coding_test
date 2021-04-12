from collections import deque # 큐 사용하기 위한 임포트

def dfs(graph, v, visited):
    visited[v] = True # 방문 표시
    print(v,end=" ")

    for i in graph[v]: # 노드에 속한 요소 탐색
        if not visited[i]: # 방문하지 않으면
            dfs(graph,i,visited) # 더 깊이 들어감

def bfs(graph, start, visited):
    queue = deque([start]) # 시작 노드추가
    visited[start] = True # 시작 방문 표시

    while queue: # 큐가 텅 빌때까지
        v = queue.popleft() # pop하고 프린트
        print(v, end = " ")

        for i in graph[v]: # pop한 노드의 요소 추가
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n,m,sn = map(int, input().split(" "))

graph = [[]]
visited_dfs = [False]*(n+1) # 방문표시 +1
visited_bfs = [False]*(n+1)

for i in range(n): # 노드만큼 리스트 요소 추가
    graph.append([])
for i in range(m): # 노드마다 서로 요소들을 추가해줌
    a,b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

for i in graph: # 제일 작은 순서대로 정렬
    i.sort()


dfs(graph,sn,visited_dfs)
print()
bfs(graph,sn,visited_bfs)