import math
def find_parent(x): # 조상 찾기
    if parent[x] != x: # 자신의 부모가 자신과 다르면 더 거슬러간다는 소리
        parent[x] = find_parent(parent[x]) # 재귀역할
    return parent[x]

def union_parent(a,b): # 합집합
    a = find_parent(a) # a의 조상찾기
    b = find_parent(b) # b의 조상 찾기
    if a < b: # a가 더 작으면
        parent[b] = a # b를 a에 연결
    else: # b가 더 작으면
        parent[a] = b # a를 b에 연결


v = int(input())
parent = [0]*v
for i in range(v): # 부모 초기화
    parent[i] = i
graph = [] # 입력 값 저장 리스트
distance = [] # (거리,시작,끝) 저장할 리스트

for i in range(v): # 입력 값 저장
    x,y = map(float, input().split(" "))
    graph.append((x,y))

for i,(sx,sy) in enumerate(graph): # 모든 별에 대해 엣지가 존재한다고 생각
    for j, (ex,ey) in enumerate(graph):
        cost = round(math.sqrt((sx-ex)**2+(sy-ey)**2),2) # 둘 사이의 거리를 구함
        distance.append((cost,i,j)) # (거리,시작,끝) 추가


distance.sort() # 거리 기준으로 정렬

result = 0
for cost,x,y in distance:
    if cost == 0: # 거리가 0이면 자기자신이기 때문에 패스
        continue
    if find_parent(x) != find_parent(y): # 부모가 다르면 합쳐준다.
        union_parent(x,y)
        result += cost # 거리를 더해줌

# print("%.2f"%result)
print(result)