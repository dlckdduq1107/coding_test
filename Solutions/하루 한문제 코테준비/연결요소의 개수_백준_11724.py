from collections import deque
#bfs할떄 처음 start에 True표시하고 연결된 노드가 visited Falsle이면 큐에 추가하고 True로 바꿔야한다.
#while문 안에서 현재노드를 True하면 이미들어간 노드가 True가 되지 않아 중복으로 들어간다.
def bfs(start):
    q = deque([])
    q.append(start)
    visited[start] = True
    while q:
        current = q.popleft()

        for i in graph[current]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
        # print(visited,current)


n,m = map(int,input().split(" "))
graph = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

result = 0
for i in range(1,n+1):
    if(not visited[i]):
        bfs(i)
        result += 1
        # print()
print(result)
