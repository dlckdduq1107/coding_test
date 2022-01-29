def check(s):
    dic = {')':'(',']':'['}
    rever_dic ={'(':')','[':']'}
    stack = []
    for char in s:
        if(char in rever_dic):
            stack.append(char)
        elif(char in dic):
            if(not stack or dic[char]!=stack.pop()):
                return False
    return len(stack) == 0

while(True):
    s = input()
    if(s=='.'):
        break
    if(check(s)):
        print('yes')
    else:
        print('no')
