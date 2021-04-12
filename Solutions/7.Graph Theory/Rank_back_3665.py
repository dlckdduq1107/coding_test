from collections import deque
def topology():
    result = [] # 결과를 출력하기 위한 리스트
    q = deque()

    for i in last: # 전체 노드중에서 진입차수가 0인거 먼저 큐에 넣어줌
        if indegree[i] == 0:
            q.append(i)

    while q: # 큐가 빌때 까지
        now = q.popleft()
        result.append(now) # 결과 리스트에 넣어줌
        for i in graph[now]:  # 현재 노드에 연결된 노드들 탐색
            indegree[i] -= 1 # 연결된 노드의 진입차수 -=
            if indegree[i] == 0: # -1 한것의 진입차수가 0이 되면 큐에 넣어줌
                q.append(i)

    if len(result) == v:
        for i in result: # 결과 출력
            print(i,end=" ")
        print()
    else: # 결과가 최종 노드수와 다르면
        print("IMPOSSIBLE")


case = int(input())
for i in range(case): # 케이스 수만큼 반복
    v = int(input())
    last = list(map(int, input().split(" ")))
    graph = [[] for j in range(v+1)]
    indegree = [0 for j in range(v+1)]
    modify = int(input())

    for j in range(v): # 지난해 입력을 그래프와 인디그리로 표현
        for w in range(j+1,v):
            graph[last[j]].append(last[w])
            indegree[last[j+1]] = j+1
    # print(graph)
    # print(indegree)
    for j in range(modify): # 수정된 수 만큼 반복
        a,b = map(int, input().split(" "))
        if b in graph[a]: # 서로의 상대적인 위치를 바꿔준다고 생각
            graph[a].remove(b)
            indegree[a] += 1
            graph[b].append(a)
            indegree[b] -= 1
        else:
            graph[b].remove(a)
            indegree[b] += 1
            graph[a].append(b)
            indegree[a] -= 1

    topology()

