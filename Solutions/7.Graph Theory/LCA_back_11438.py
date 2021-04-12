import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))
def dfs(x,depth): # 루트 부터 시작해서 깊이를 구하는 함수
    c[x] = True
    d[x] = depth

    for i in graph[x]:
        if c[i]:
            continue
        parent[i][0] = x
        dfs(i,depth+1)

def set_parent(): # 전체 부모의 관계 설정
    dfs(1,0) # 루트노드
    for i in range(1,LOG):
        for j in range(1,v+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def lca(a,b): # 최소 공통 조상
    if d[a] > d[b]: # b가 더 깊도록 설정
        a,b = b,a
    for i in range(LOG-1,-1,-1): # 깊이가 동일 하도록 맞춰줌
        if d[b] -d[a] >= (1<<i):
            b = parent[b][i]
    if a == b: # 부모가 같아지도록
        return a
    for i in range(LOG-1,-1,-1): # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]

v = int(input())

LOG = 21

parent = [[0] *LOG for i in range(v+1)] # 아마 한 노드에 LOG씩 차례대로 조사을 저장하는 거 같음
d = [0] *(v+1) # 깊이를 저장하는 리스트
c = [0]*(v+1) # 깊이 체크 여부를 저장하는 리스트
graph = [[] for i in range(v+1)] # 그래프 입력

for i in range(v-1): # 입력을 그래프로 변환
    a,b = map(int,input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

set_parent()

m = int(input())
for i in range(m):
    a,b = map(int,input().split(" "))
    print(lca(a,b))
