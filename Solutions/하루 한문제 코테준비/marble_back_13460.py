from collections import deque

def dfs(rx,ry,bx,by):
    q = deque()
    q.append((rx,ry,bx,by))
    visited = [] # 중복 위치 저장 위함
    visited.append((rx,ry,bx,by))
    count = 0

    while q:
        for w in range(len(q)): # 큐에 있는거 다빼는 용도
            rx,ry,bx,by = q.popleft() # 구슬 위치

            if count > 10: # 10이 넘어가면
                print(-1)
                return

            if graph[rx][ry] == "O": # 현재 구슬 위치가 O이면
                print(count)
                return

            for i in range(4): # 4방향 탐색
                nrx,nry = rx,ry # 빨간 구슬 위치
                while True: # #을 만나거나 O를 만날때 까지  특정방향으로 이동
                    nrx += dx[i]
                    nry += dy[i]
                    if graph[nrx][nry] == "#": # #만나면 만나기 이전위치가 빨간 구슬의 위치가 됨
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if graph[nrx][nry] == "O": # O를 만나면 빨간 구슬이 구멍을 만난것임
                        break

                nbx,nby = bx,by # 파란 구슬의 위치
                while True:# #을 만나거나 O를 만날때 까지  특정방향으로 이동
                    nbx += dx[i]
                    nby += dy[i]
                    if graph[nbx][nby] == "#":# #만나면 만나기 이전위치가 파란 구슬의 위치가 됨
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if graph[nbx][nby] == "O": # O를 만나면 파란 구슬이 구멍을 만난것임
                        break


                if graph[nbx][nby] == "O": # 파란구슬이 구멍에 있으면 그 방향은 실패한 방향임
                    continue # 다음 방향으로 넘어감

                if nrx == nbx and nry == nby: # 도착 위치가 같을때는 멀리서온 구슬이 한칸 이전으로 가야함
                    if abs(rx-nrx) + abs(ry-nry) < abs(bx-nbx) + abs(by-nby):
                        nbx -= dx[i]
                        nby -= dy[i]
                    else:
                        nrx -= dx[i]
                        nry -= dy[i]

                if (nrx,nry,nbx,nby) not in visited: # 방문 하지 않았던 곳이면
                    q.append((nrx,nry,nbx,nby))
                    visited.append((nrx,nry,nbx,nby))


        count += 1
    print(-1) # 사방이 막혀있어 아무것도 하지 못할때



#4방향 탐색
dx = [0,0,1,-1]
dy = [1,-1,0,0]

n,m = map(int, input().split(" "))

graph = []

for i in range(n):
    graph.append(list(input()))
    for j in range(m): # 구슬 위치 저장
        if graph[i][j] == "R":
            rx,ry = i,j
        if graph[i][j] == "B":
            bx,by = i,j


dfs(rx,ry,bx,by)

