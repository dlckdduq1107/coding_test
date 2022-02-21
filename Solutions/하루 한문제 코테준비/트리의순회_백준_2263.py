import sys
sys.setrecursionlimit(10**5)
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

dfs(in_order,post)