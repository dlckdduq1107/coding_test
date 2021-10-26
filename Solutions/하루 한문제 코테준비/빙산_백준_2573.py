import copy
from collections import deque
def bfs():
    q = deque([])

n,m = map(int,input().split(" "))
graph = []
dx,dy = [0,0,1,-1],[1,-1,0,0]
for i in range(n):
    graph.append(list(map(int,input().split(" "))))

while(1):
    temp = []
    for i in range(1,n-1):
        for j in range(m):
            if(0<=i<n and 0<=j<m and graph[i][j]!=0):
                count = 0
                for q in range(4):
                    nx,ny = i+dx[q],j+dy[q]
                    if(graph[nx][ny]==0):
                        count+=155
                    #카운트세서 temp에 추가 한다음(x,y,숫자) temp안에 있는거 반복하면서 graph에 반영하고 bfs로 찾기 한번 더 찾아지면 break, 안나눠지는 경우는 생각해야됨

