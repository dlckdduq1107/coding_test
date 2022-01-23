
n = int(input())

dp_min = [0 for i in range(3)]
dp_max = [0 for i in range(3)]
temp_min = [0 for i in range(3)]
temp_max = [0 for i in range(3)]
for i in range(n):
    a,b,c = map(int,input().split(" "))

    for j in range(3):
        if(j==0):
            temp_min[j] = a+min(dp_min[j],dp_min[j+1])
            temp_max[j] = a+max(dp_max[j],dp_max[j+1])
        elif(j==1):
            temp_min[j] = b+min(dp_min[j],dp_min[j-1],dp_min[j+1])
            temp_max[j] = b+max(dp_max[j],dp_max[j-1],dp_max[j+1])
        else:
            temp_min[j] = c+min(dp_min[j],dp_min[j-1])
            temp_max[j] = c+max(dp_max[j],dp_max[j-1])
    for j in range(3):
        dp_min[j] = temp_min[j]
        dp_max[j] = temp_max[j]

print(max(dp_max),min(dp_min))
# print(dp_max)