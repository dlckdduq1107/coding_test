string = input().upper()

# string.sort()
result = {}

for i in string:
    if(i in result):
        result[i] += 1
    else:
        result[i] = 1

temp = 0
flag = False
for i in result:
    if(result[i]>temp):
        a = i
        temp = result[i]
        flag = False
    elif(result[i]==temp):
        flag = True

if(flag):
    print('?')
else:
    print(a)
