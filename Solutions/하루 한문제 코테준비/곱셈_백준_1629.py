def divide(q,w):
    if(w==1):
        return q%c
    else:
        temp = divide(q,w//2)

        if(w%2==0):
            return temp*temp%c
        else:
            return temp*temp*a%c


a,b,c = map(int,input().split())
# num = [a for i in range(b)]
print(divide(a,b))