whole_str = input()
bomb = input()
bomb_length = len(bomb)

stack = []

for i in whole_str:
    stack.append(i)
    if(len(stack)<bomb_length):
        continue
    if(''.join(stack[-bomb_length:]) == bomb):
        for j in range(bomb_length):
            stack.pop()
    # print(stack)
if(len(stack)==0):
    print("FRULA")
else:
    print(''.join(stack))
