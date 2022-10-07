ppap = input()

stack = []

for i in ppap:
    stack.append(i)
    if(len(stack)>3 and ''.join(stack[-4:]) == "PPAP"):
        for j in range(3):
            stack.pop()

result = ''.join(stack[:])
if(result == "P" or result == "PPAP"):
    print("PPAP")
else:
    print("NP")
