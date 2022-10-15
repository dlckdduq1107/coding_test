n,p = map(int,input().split(" "))

stack = [[] for i in range(n+1)]

result = 0
# print(stack)
for i in range(n):
    num,flat = map(int,input().split(" "))
    if(len(stack[num])==0):
        stack[num].append(flat)
        result += 1
    else:
        # print(stack[num][-1])
        last = stack[num][-1]
        if(flat > last):
            stack[num].append(flat)
            result += 1
        elif(flat < last):
            while(True):
                if(len(stack[num]) ==0):
                    stack[num].append(flat)
                    result += 1
                    break
                last = stack[num][-1]
                if(last <= flat):
                    if(last < flat):
                        stack[num].append(flat)
                        result += 1
                    break
                stack[num].pop()
                result += 1
            
    # print(result)
print(result)

