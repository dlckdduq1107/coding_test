n,k = map(int,input().split(" "))
heights = list(map(int,input().split(" ")))

differ = []
# heights.sort()
for i in range(n):
    if(i==0):
        continue
    else:
        differ.append(heights[i]-heights[i-1])
# print(differ)
differ.sort()
print(sum(differ[:n-k]))