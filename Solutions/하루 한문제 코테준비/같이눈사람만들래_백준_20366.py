n = int(input())
snow = list(map(int,input().split(" ")))
snow.sort()
result = int(1e9)
for i in range(n):
    for j in range(i+3,n):
        start,end = i+1,j-1
        fisrt_snowman = snow[i]+snow[j]
        while(start<=end):
            temp = snow[start]+snow[end]
            result = min(result,abs(fisrt_snowman-temp))
            if(fisrt_snowman-temp>0):
                start += 1
            else:
                end -= 1

print(result)