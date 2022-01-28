n = int(input())

for i in range(n):
    num = int(input())
    result = [[0,0] for j in range(num+1)]
    result[0] = [1,0]
    if(num>0):
        result[1] = [0,1]
    if(num<2):
        print(' '.join(list(map(str,result[num]))))
    else:
        for q in range(2,num+1):
            result[q][0] = result[q-1][0]+result[q-2][0]
            result[q][1] = result[q-1][1]+result[q-2][1]
        # print(result)
        print(' '.join(list(map(str,result[num]))))


