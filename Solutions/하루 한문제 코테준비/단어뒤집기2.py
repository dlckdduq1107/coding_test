s = input()

stack = []
tag_flag = False
temp_str = []
for idx,i in enumerate(s):
    if(i=='<'):
        for j in range(len(temp_str)):
            stack.append(temp_str.pop())
        tag_flag = True
        stack.append(i)
        continue
    elif(i=='>'):
        tag_flag = False
        stack.append(i)
        continue

    if(tag_flag):
        stack.append(i)
    else:
        if(i==' '):
            for j in range(len(temp_str)):
                stack.append(temp_str.pop())
            stack.append(i)
        else:
            temp_str.append(i)
if(len(temp_str) != 0):
    for j in range(len(temp_str)):
        stack.append(temp_str.pop())
print(''.join(stack))
            
