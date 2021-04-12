import heapq
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start,0))
    distance[start] = 0
    charge[start] = 0

    while q:
        cos, now, dist = heapq.heappop(q)
        if charge[now] < cos:
            continue
        for i in graph[now]:
            cost = charge[now]+i[1]
            if cost < charge[i[0]]:
                charge[i[0]] = cost
                distance[i[0]] = distance[now] + i[2]
                heapq.heappush(q,(cost,i[0],distance[i[0]]))



case = int(input())
INF = int(1e9)
for i in range(case):
    v,max_cost,e = map(int, input().split(" "))
    graph = [[] for i in range(v+1)]
    matrix = [[INF]*(v+1) for q in range(max_cost+1)]

    for j in range(e):
        a,b,c,d = map(int, input().split(" "))
        graph[a].append((b,c,d))

    for j in range(max_cost):
        distance = [INF] * (v + 1)
        charge = [INF] * (v + 1)
        dijkstra(1)
        for q in range(v+1):
            if charge[q] == j:
                matrix[j][q] = distance[q]

    res = INF
    for q in matrix:
        if q[v] < res:
            res = q[v]

    if res == INF:
        print("Poor KCM")
    else:
        print(res)

