import sys
sys.setrecursionlimit(10**5) # 재귀 리미트를 걸여줘야 맞게 판단됨

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

input = sys.stdin.readline
v,e = map(int,input().split())
parent = [0]*(v+1)
for i in range(v+1): # 조상을 자기 자신으로 초기화
    parent[i] = i

for i in range(e):
    q,w,e =  map(int,input().split(" "))
    if q == 0:
        union_parent(w,e)
    else:
        fa = find_parent(w)
        fb = find_parent(e)
        if fa == fb:
            print("YES")
        else:
            print("NO")

