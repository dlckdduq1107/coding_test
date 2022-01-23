def recur(num, shape):
    result = []
    if(num==3):
        return shape
    for i in shape:
        result.append(i*3)
    for i in shape:
        result.append(i+' '*len(i)+i)
    for i in shape:
        result.append(i*3)

    return recur(num//3,result)

n = int(input())
shape = ['***','* *','***']
res = recur(n,shape)
for i in res:
    print(i)