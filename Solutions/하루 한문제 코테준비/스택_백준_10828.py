from collections import deque
import sys
n = int(sys.stdin.readline())

stack = deque([])
for i in range(n):
    order = sys.stdin.readline().split()
    # print(order)
    if(order[0]=='push'):
        stack.append(order[1])
    elif(order[0]=='pop'):
        if(stack):
            print(stack.pop())
        else:
            print(-1)
    elif(order[0]=='size'):
        print(len(stack))
    elif(order[0]=='empty'):
        if(stack):
            print(0)
        else:
            print(1)
    elif(order[0]=='top'):
        if(stack):
            print(stack[-1])
        else:
            print(-1)