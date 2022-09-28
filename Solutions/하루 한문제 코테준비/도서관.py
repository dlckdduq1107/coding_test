n,limit = map(int,input().split(" "))
books = list(map(int,input().split(" ")))
minus,plus = [],[]
for i in books:
    minus.append(i) if i<0 else plus.append(i)

minus.sort()
plus.sort(reverse=True)
max_minus = 0 if len(minus)==0 else abs(min(minus))
max_plus = 0 if len(plus)==0 else max(plus)

result = 0

if(max_minus >= max_plus):
    if(max_minus==max_plus):
        if(len(minus)>len(plus)):
            full_search_list = plus
            second = minus
        else:
            full_search_list = minus
            second = plus
    else:
        full_search_list = plus
        second = minus
else:
    full_search_list = minus
    second = plus

i = 0

while(i<len(full_search_list)):
    result += abs(full_search_list[i]*2)
    if(i+limit>=len(full_search_list)):
        i=len(full_search_list)
    else:
        i+=limit
# print(result)
j = 0
while(j<len(second)):
    if(j==0):
        result += abs(second[j])
    else:
        result += abs(second[j]*2)
    if(j+limit>=len(second)):
        j=len(second)
    else:
        j+=limit
    # print(result)
print(result) 