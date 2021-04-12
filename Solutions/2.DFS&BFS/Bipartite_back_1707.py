from collections import deque
####맞게 한거 같은데 왜 틀린지 모름#####
def bfs(graph, start, visited,vertics):
    queue = deque()
    queue.append((start))
    visited[start] = True

    c = [1,-1] # 색 차례대로 넣어주기 위한 것
    color = 0
    vertics[start] = c[color]
    color += 1

    while queue:
        q = queue.popleft()
        for i in graph[q]:
            if visited[i] == False: # 탐색안한 부분일때 탐색하고 색 넣어주기
                visited[i] = True
                queue.append(i)
                vertics[i] = c[color%2]

            else: # 트루일때 같은지 검사
                if vertics[i] == vertics[q]:
                    return "NO"
        color += 1
    return "YES"

case_num = int(input())
case_list = []
for _ in range(case_num):
    graph = [[]]
    v,e = map(int, input().split(" "))
    vertics = [0]*(v+1)
    visited = [False] * (v + 1)

    for i in range(v):
        graph.append([])
    for i in range(e):
        e1,e2 = map(int,input().split(" "))
        graph[e1].append(e2)
        graph[e2].append(e1)

    case_list.append(bfs(graph,1,visited,vertics))

for i in case_list:
    print(i)