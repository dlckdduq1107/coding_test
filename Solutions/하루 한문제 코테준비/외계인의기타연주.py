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
            while(flat < last):
                result += 1
                stack[num].pop(-1)
                if(len(stack[num]) ==0):
                    stack[num].append(flat)
                    last = flat
                    result += 1
                else:
                    last = stack[num][-1]
            if(flat != last):
                result += 1
    # print(result)
print(result)

