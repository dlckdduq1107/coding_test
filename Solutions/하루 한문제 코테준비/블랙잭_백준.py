n,m = map(int,input().split(' '))
num = list(map(int,input().split(" ")))
num.sort()
result = m
for i in range(len(num)-2):
    for j in range(i+1,len(num)-1):
        for q in range(j+1,len(num)):
            sum_num = num[i]+num[j]+num[q]
            if(sum_num>m):
                continue
            if( m-sum_num<result):
                result = m-sum_num
print(m-result)