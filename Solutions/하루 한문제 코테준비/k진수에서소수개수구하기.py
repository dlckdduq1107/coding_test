def convert(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 
def is_prime(n):
    for i in range(2,int(n**(0.5))+1):
        if(n%i==0):
            return False
    return True

def solution(n, k):
    answer = 0
    change = convert(n,k)
    words = change.split('0')
    change = int(change)
    
    for i in words:
        if(i == ''):
            continue
        if(int(i)<2):
            continue
        if(is_prime(int(i))):
            answer += 1
    return answer
print(solution(437674,3))