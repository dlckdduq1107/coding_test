n = int(input())
result = n
for i in range(n):
    s = input()
    for j in range(len(s)-1):
        if(s.find(s[j])>s.find(s[j+1])):
            result -= 1
            break
print(result)