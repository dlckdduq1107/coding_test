n = int(input())
q = []
order = []
for i in range(n):
    num = int(input())
    q.append(num)
    order.append(num)

q.sort(reverse=True)
stack = []
result = []
flag = False
for i in order:
    # print(stack,q,i)
    if(stack and stack[-1]>i):
        flag = True
        break
    while(q and i>=q[-1]):
        stack.append(q.pop())
        result.append('+')
    if(stack and stack[-1]==i):
        stack.pop()
        result.append('-')

    # print(stack,q)
    # print()

if(flag):
    print("NO")
else:
    for i in result:
        print(i)