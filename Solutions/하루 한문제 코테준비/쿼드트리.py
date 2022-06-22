def divide(arr):    
    target = arr[0][0]
    flag = False
    for i in arr:
        for j in i:
            if(j != target):
                flag = True
                break
        if(flag):
            break
    if(flag):
        term = len(arr)//2
        print('(',end='')
        divide([i[:term*1] for i in arr[:term*1]])
        divide([i[term*1:term*2] for i in arr[:term*1]])

        divide([i[:term*1] for i in arr[term*1:term*2]])
        divide([i[term*1:term*2] for i in arr[term*1:term*2]])
        print(')',end='')
    else:
        print(target, end='')
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,list(input()))))

divide(graph)