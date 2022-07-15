n = int(input())
edges = int(input())
graph = [[] for i in range(n+1)]
distance = []
for i in range(edges):
    start, end, cost = map(int, input().split(" "))
    distance.append([start,end,cost])
distance.sort(key=lambda x:x[2])

result = 0
cycle = set()
# s,e,c = distance.pop(0)
# cycle.extend([s,e])
# result += c
for start,end,cost in distance:
    if(len(cycle)==n):
        break
    if(start in cycle and end in cycle):
        continue
    else:
        cycle.add(start)
        cycle.add(end)
        result += cost
        print(start,end,cycle,result)
print(result)