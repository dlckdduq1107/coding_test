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
num = int(input())
parent = [0]*(v+1)
for i in range(v+1): # 조상을 자기 자신으로 초기화
    parent[i] = i

for i in range(v):
    q = list(map(int,input().split(" ")))
    for j in range(len(q)):
        if q[j] == 1:
            union_parent(i+1,j+1)

p = list(map(int,input().split(" ")))
rout = find_parent(p[0])
for i in p[1:]:
    if find_parent(i) != rout:
        print("NO")
        exit(0)
print("YES")