sticks = input()
count = 0
stack = []

result = 0
flag = False
for i in sticks:
    stack.append(i)
    if(i=='('):
        result += 1
        count += 1
        

    else:
        if(''.join(stack[-2:]) == '()'):
            result -= 1
            count -= 1
            result += count
            # if(not flag and count>0):
            #     result += count
            #     flag = True
        else:
            count -= 1
            
    # print(i,count,result)
print(result)

