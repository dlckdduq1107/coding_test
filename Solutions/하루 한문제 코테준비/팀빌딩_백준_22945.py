n = int(input())
arr = list(map(int,input().split(" ")))
start,end = 0,n-1

result = -1
while(start<=end):
    result = max(result,(end-start-1)*min(arr[start],arr[end]))
    if(arr[start]>arr[end]):
        end -= 1
    else:
        start += 1

print(result)