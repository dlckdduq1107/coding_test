gal = input()
result = 0
temp = 1
stack = []
for i in gal:
    if(i =='('):
        temp *=2
        stack.append(i)
    elif(i==')'):
        if(not stack and stack[-1]=='['):
            result = 0
            break
            
        if(stack[-1]=='('):
            result += temp
            temp //=2
            stack.pop()

    elif(i=='['):
        temp *=3
        stack.append(i)
    elif(i==']'):
        if(not stack and stack[-1]=='('):
            result = 0
            break
            
        else:
            result += temp
            temp//=3
            stack.pop()
    print(stack,result)
if( stack):
    print(0)
else:
    print(result)

