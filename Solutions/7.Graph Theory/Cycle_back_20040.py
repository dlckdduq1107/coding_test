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
parent = [0]*v
for i in range(v):
    parent[i] = i

cycle = False

for i in range(e):
    a,b = map(int,input().split(" "))
    if find_parent(a) == find_parent(b):
        cycle = True
        print(i+1)
        break
    else:
        union_parent(a,b)

if not cycle:
    print(0)