n = int(input())

is_prime = [True for i in range(n+1)]
for i in range(2, int(n**0.5)+1):
    if(is_prime[i]):
        for j in range(i*2,n+1,i):
            is_prime[j] = False

prime_list = []
for i in range(2,len(is_prime)):
    if(is_prime[i]):
        prime_list.append(i)

sum_prime = [0 for i in range(len(prime_list)+1)]
for i in range(len(prime_list)):
    sum_prime[i+1] = sum_prime[i]+prime_list[i] 

result = 0
start = 0
end = 1
while(start<len(sum_prime) and end < len(sum_prime)):
    if(sum_prime[end]-sum_prime[start]==n):
        result += 1
        start += 1
    elif(sum_prime[end]-sum_prime[start]>n):
        start += 1
    else:
        if(end<len(sum_prime)):
            end+=1
        else:
            start += 1
print(result)
