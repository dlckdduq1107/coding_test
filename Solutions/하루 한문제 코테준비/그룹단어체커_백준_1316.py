n = int(input())
result = 0
for i in range(n):
    s = input()
    duple = []

    pre = s[0]
    for idx,each in enumerate(s):
        if(idx==0):
            if(idx==len(s)-1):
                result += 1
            continue
        if(each in duple):
            break
        else:
            if(each != pre):
                duple.append(pre)

        if(idx==len(s)-1):
            result += 1
        pre = each
print(result)