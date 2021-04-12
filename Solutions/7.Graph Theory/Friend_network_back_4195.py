def find_parent(x): # 조상 찾기
    if parent[x] != x: # 자신의 부모가 자신과 다르면 더 거슬러간다는 소리
        parent[x] = find_parent(parent[x]) # 재귀역할
    return parent[x]

def union_parent(a,b): # 합집합
    a = find_parent(a) # a의 조상찾기
    b = find_parent(b) # b의 조상 찾기
    if a != b: # 다르면
        parent[b] = a # b의 부모를 a로 업데이트
        number[a] += number[b] # b에 대한 노드 개수를 a가 흡수

case = int(input())
for q in range(case):
    e = int(input())
    parent = {}
    number = {}
    for i in range(e):
        f1,f2 = map(str, input().split(" "))

        if f1 not in parent: # 처음들어왔을때
            parent[f1] = f1
            number[f1] = 1
        if f2 not in parent:# 처음들어왔을때
            parent[f2] = f2
            number[f2] = 1

        union_parent(f1,f2)
        print(number[find_parent(f1)])#f1의 부모를 찾아 number출력

