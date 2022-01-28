dic = {')':'('}
n = int(input())
for i in range(n):
    stack = []
    string = input()
    flag = False
    for s in string:
        if(s not in dic):
            stack.append(s)
        else:
            if(not stack or dic[s]!=stack.pop()):
                flag = True
                print("NO")
                break
    # print(stack,i)
    if(flag):
        continue
    else:
        if(stack):
            print("NO")
        else:
            print("YES")

