def divideQ(arr):
    target = arr[0][0]
    flag = False
    for i in arr:
        for j in i:
            if(target!=j):
                flag = True
                break
        if(flag):
            break
    
    if(flag):
        term = len(arr)//3

        divideQ([i[:term*1] for i in arr[:term*1]])
        divideQ([i[:term*1] for i in arr[term*1:term*2]])
        divideQ([i[:term*1] for i in arr[term*2:term*3]])

        divideQ([i[term*1:term*2] for i in arr[:term*1]])
        divideQ([i[term*1:term*2] for i in arr[term*1:term*2]])
        divideQ([i[term*1:term*2] for i in arr[term*2:term*3]])

        divideQ([i[term*2:] for i in arr[:term*1]])
        divideQ([i[term*2:] for i in arr[term*1:term*2]])
        divideQ([i[term*2:] for i in arr[term*2:term*3]])
    else:
        result[target] += 1

n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int,input().split(" "))))

result = {-1:0,0:0,1:0}

divideQ(paper)

for i in [-1,0,1]:
    print(result[i])