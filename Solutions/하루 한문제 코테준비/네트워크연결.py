def union(a,b):
    root1 = find(a)
    root2 = find(b)
    if(root1>root2):
        parent[root1] = root2
    else:
        parent[root2] = root1

def find(node):
    if(parent[node]!=node):
        parent[node] = find(parent[node])
    return parent[node]

n = int(input())
parent = [i for i in range(n+1)]
edges = int(input())
distance = []
for i in range(edges):
    start, end, cost = map(int, input().split(" "))
    distance.append([start,end,cost])
distance.sort(key=lambda x:x[2])

result = 0
for start,end,cost in distance:
    if(find(start) != find(end)):
        union(start,end)
        result += cost
print(result)