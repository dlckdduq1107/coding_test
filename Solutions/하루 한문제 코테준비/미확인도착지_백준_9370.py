import heapq
def dijktra(start):
    distance = [int(1e9)]*(n+1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)
        if(distance[now]<dist):
            continue
        for next in graph[now]:
            cost = dist + next[1]
            if(cost < distance[next[0]]):
                distance[next[0]] = cost
                heapq.heappush(q,(cost,next[0]))
                check[next[0]].append(now)
    return distance

t = int(input())

for i in range(t):
    n,m,count = map(int,input().split())
    s,g,h = map(int,input().split())
    graph = [[] for j in range(n+1)]
    for j in range(m):
        a,b,d = map(int,input().split())
        graph[a].append([b,d])
        graph[b].append([a,d])
    destination = []
    for j in range(count):
        destination.append(int(input()))

    check = [[] for j in range(n+1)]
    total = dijktra(s)
    start_g = dijktra(g)
    start_h = dijktra(h)

    result = []
    for d in destination:
        if(total[d]==total[g]+start_g[h]+start_h[d] or total[d]==total[h]+start_h[g]+start_g[d]):
            result.append(d)

    result.sort()
    print(*result)