import sys
sys.setrecursionlimit(10**6)
def dfs(inorder,postorder):
    if(inorder==[] or postorder==[]):
        return
    if(len(inorder)==1):
        print(inorder[0],end=" ")
        return

    center = postorder[-1]
    print(center,end=" ")

    idx = inorder.index(center)
    first_in = inorder[:idx]
    second_in = inorder[idx+1:]
    first_post = postorder[:idx]
    second_post = postorder[idx:-1]

    dfs(first_in,first_post)
    dfs(second_in,second_post)




n = int(input())

in_order = list(map(int,input().split()))
post = list(map(int,input().split()))

# dfs(in_order,post)

pos = [0]*(n+1)
for i in range(n):
    pos[in_order[i]] = i # 전위 순회

def divide(in_start, in_end, p_start, p_end):
    if(in_start > in_end) or (p_start > p_end):
        return
    parents = post[p_end] # 후위순회에서 부모노드 찾기
    print(parents, end=" ")
    left = pos[parents] - in_start # 왼쪽인자 갯수
    right = in_end - pos[parents] # 오른쪽인자 갯수
    divide(in_start, in_start+left-1, p_start, p_start+left-1) # 왼쪽 노드
    divide(in_end-right+1, in_end, p_end-right, p_end-1) # 오른쪽 노드

divide(0,n-1,0,n-1)