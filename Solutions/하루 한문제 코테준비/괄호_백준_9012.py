def check(s):
    stack = []
    for char in s:
        if(char not in dic):
            stack.append(char)
        else:
            if(not stack or dic[char]!=stack.pop()):
                return False

    return len(stack)==0

dic = {')':'('}
n = int(input())
for i in range(n):
    string = input()
    if(check(string)):
        print("YES")
    else:
        print("NO")

