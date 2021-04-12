def dfs(graph, v, visited):
    visited[v] = True
    graph[0][0] += 1 # 그래프의 첫부분을 카운트로 사용함

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

n = int(input())
m = int(input())

graph = [[0]] # 처음요소는 카운트하는 변수로 사용
visited = [False]*(n+1) # 방문표시 +1


for i in range(n): # 노드만큼 리스트 요소 추가
    graph.append([])
for i in range(m): # 노드마다 서로 요소들을 추가해줌
    a,b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

dfs(graph,1,visited)
print(graph[0][0]-1) # 처음노드는 제외하고 개수 출력