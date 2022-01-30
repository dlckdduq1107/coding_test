import collections
from collections import Counter
def div(arr):
    target = arr[0][0]
    flag = False
    for i in arr:
        for j in i:
            if(j!= target):
                flag = True
                break
        if(flag):
            break

    if(flag):
        wall = len(arr)//3
        div([i[:wall*1] for i in arr[:wall*1]])
        div([i[:wall*1] for i in arr[wall*1:wall*2]])
        div([i[:wall*1] for i in arr[wall*2:wall*3]])

        div([i[wall*1:wall*2] for i in arr[:wall*1]])
        div([i[wall*1:wall*2] for i in arr[wall*1:wall*2]])
        div([i[wall*1:wall*2] for i in arr[wall*2:wall*3]])

        div([i[wall*2:wall*3] for i in arr[:wall*1]])
        div([i[wall*2:wall*3] for i in arr[wall*1:wall*2]])
        div([i[wall*2:wall*3] for i in arr[wall*2:wall*3]])

    else:
        result[target] += 1


result = {-1:0,0:0,1:0}
n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int,input().split(" "))))

div(graph)

for i in sorted(result):
    print(result[i])