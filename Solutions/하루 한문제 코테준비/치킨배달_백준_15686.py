from itertools import combinations

def calDistance(hx,hy):
    res = int(1e9)
    for i in range(n):
        for j in range(n):
            if(graph[i][j]==2):
                res = min(res,abs(hx-i)+abs(hy-j))
    return res

n,m = map(int,input().split(" "))
graph = []
home = []
chicken = []
result = int(1e9)
for i in range(n):
    graph.append(list(map(int,input().split(" "))))
for i in range(n):
    for j in range(n):
        if(graph[i][j]==1): home.append((i,j))
        if(graph[i][j]==2): chicken.append((i,j))

for i in combinations(chicken,m):
    temp = 0
    for h in home:
        temp += min(abs(h[0]-c[0])+abs(h[1]-c[1]) for c in i)
    result = min(result,temp)

print(result)


