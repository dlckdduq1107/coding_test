import copy
from collections import deque
import sys
input = sys.stdin.readline
def connection():
    target = 0
    m = 0
    for i in range(1,n+1):
        tempGraph = copy.deepcopy(graph)
        a = i
        res = 0
        if(tempGraph[a] == 0):
            continue
        while tempGraph[a] != 0:
            tt = tempGraph[a]
            tempGraph[a] = 0
            a = tt
            res += 1
        if(m<res):
            m = res
            target = i
    return target


n = int(input())
graph = deque([0])
graph.extend(list(map(int,input().split(" "))))

result = deque([])
nex = -1
temp = 0

while sum(graph) != 0:
    if(nex==-1):
        nex = graph[1]
        graph[1] = 0
        result.append(nex)
    else:
        nex = connection()
        result.append(nex)
    while nex != 0:
        if(graph[nex]==0):
            break
        temp = nex
        nex = graph[nex]
        graph[temp] = 0
        if(nex != 0):
            result.append(nex)

print(len(result))
for idx,i in enumerate(result):
    if idx == len(result)-1:
        print(i)
    else:
        print(i,end=" ")



