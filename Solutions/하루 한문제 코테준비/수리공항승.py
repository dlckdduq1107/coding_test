n,tape = map(int,input().split(" "))
location = list(map(int,input().split(" ")))
result = 0
location.sort()
i = 0
while(i<len(location)):
    temp_i = i+tape-1
    if(temp_i>=len(location)):
        temp_i = len(location)-1
    next_i = i
    for j in range(temp_i,i,-1):
        if(location[j]-location[i] <= tape-1):
            next_i = j
            break

    result += 1
    if(next_i==i):
        i+= 1
    else:
        i = next_i+1
    # print("i",i,"next",next_i)
print(result)