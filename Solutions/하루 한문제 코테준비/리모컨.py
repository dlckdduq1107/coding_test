n = int(input())
error_key = int(input())
if(error_key != 0):
    error_list = list(map(int,input().split(" ")))
    min_count = abs(100-n)

    for i in range(1000001):
        temp = str(i)
        for jdx,j in enumerate(temp):
            if(int(j) in error_list):
                break
            if(jdx == len(temp)-1):
                min_count = min(min_count,abs(i-n)+len(temp))
    print(min_count)
            
else:
    print(min(abs(100-n),len(str(n))))