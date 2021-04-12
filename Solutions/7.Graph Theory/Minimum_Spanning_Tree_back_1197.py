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

v,e = map(int, input().split(" "))
parent = [0]*(v+1)
for i in range(v+1):
    parent[i] = i
edge = []
result = 0

for i in range(e): # 비용을 포함한 입력 저장
    a,b,cost = map(int, input().split(" "))
    edge.append((cost,a,b))

edge.sort() # 비용순으로 정렬

for cost,a,b in edge: # 모든 엣지를 대상으로
    if find_parent(a) != find_parent(b): # 부모가 다르면 사이클 존재x 이므로 유니온
        union_parent(a,b)
        result += cost

print(result)