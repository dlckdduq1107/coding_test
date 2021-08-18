n = int(input())
graph = [[0 for i in range(n)] for j in range(n)]
k = int(input())

for i in range(k):
    a,b = map(int, input().split(" "))
    a,b = a-1,b-1
    graph[a][b] = 1

l = int(input())
direct = []
for i in range(l):
    a,b = input().split(" ")
    direct.append((int(a), b))

## 동작 순서에 맞게 반복문 수정해야함
time = 1
x,y = 0,1
graph[0][0] = 2
dx,dy = 0,1 # 방향표시
tx,ty = 0,0 # 꼬리 표시
while(0<= x < n and 0<= y < n and graph[x][y] != 2): # 범위 안벗어나고 자기자신 아니면
    time += 1
    x,y = x+dx,y+dy # 한칸 이동
    if graph[x][y] == 1: # 사과이면
        graph[x][y] = 2
    elif graph[x][y] == 0: # 그냥이면
        graph[tx][ty] = 0 #꼬리 0으로 하고
        tx,ty = tx+dx, ty+dy # 한칸옮긴거를 꼬리로
        graph[x][y] = 2 # 머리는 2로

    if direct[0][0] == time: # time이랑 방향 바뀌는 시간 같으면
        a,b = direct.pop(0)

         # 방향에 따라 바뀌는 규칙이 있음
        if dx != 0:
            if b == 'L':
                dx,dy = dy,dx
            elif b == 'D':
                dx,dy = dy,-dx
        else:
            if b == 'L':
                dx,dy = -dy,dx
            elif b == 'D':
                dx,dy = dy,dx

print(time)