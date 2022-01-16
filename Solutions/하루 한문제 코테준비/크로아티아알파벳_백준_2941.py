s = input()

croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

result = 0
pivot = 0
while(pivot<len(s)):
    if(pivot+3>len(s)):
        if(pivot+3-len(s)==1):
            if(s[pivot:pivot+2] in croatia):
                result += 1
            else:
                result += 2
            break
        elif(pivot+3-len(s)==2):
            result += 1
            break
    third = s[pivot:pivot+3]
    if(third in croatia):
        result += 1
        pivot += 3
    else:
        second = s[pivot:pivot+2]
        if(second in croatia):
            result += 1
            pivot += 2
        else:
            result += 1
            pivot +=1

print(result)