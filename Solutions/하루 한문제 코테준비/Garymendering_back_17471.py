def dfs(cnt, nodes, size): ##nodes는 현재 그룹안에 어떤 노드가 포함되어있는지에 대한 변수, size는 그룹의 크기에 대한 변수
    global result

    if cnt == size: # 그룹의 크기가  같아지면
        ##그룹별로 인덱스 리스트 만들어 나눠주고
    ## 연결되어있는지 판단한 다음
     # 최소값 업데이트


    for i in range(nodes,n+1): # 크기에 따라 나오는 선택하는 노드 경우의 수를 하나하나씩 탐색(크기가 2일때 1,2해보고 1,3해보고 1,4해보고)
        if dup[i]:
            continue

        dup[i] = 1
        dfs(cnt+1, i,size)
        dup[i] = 0


n = int(input())
human_list = [0]+list(map(int,input().split(" ")))
graph = [[] for i in range(n+1)]
connect = [0 for i in range(n+1)]
for i in range(n):
    a = list(map(int, input().split(" ")))
    if a[0] != 0:
        connect[i] = a[0]
        graph[i] = a[1:]
    else:
        connect[i] = a[0]


result = int(1e9)

for i in range(1,n+1): # 1~n까지 크기를 반복
    dup = [0 for j in range(n+1)]
    dfs(0,1,i)