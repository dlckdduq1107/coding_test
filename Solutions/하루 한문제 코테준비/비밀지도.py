def solution(n, arr1, arr2):
    answer = []
    arr1_cpy,arr2_cpy = [],[]
    for i in arr1:
        two = str(bin(i))[2:]
        arr1_cpy.append(two if len(two)==n else '0'*(n-len(two))+two)
    for i in arr2:
        two = str(bin(i))[2:]
        arr2_cpy.append(two if len(two)==n else '0'*(n-len(two))+two)
        
    for i in range(n):
        arr1_row = list(map(int,arr1_cpy[i]))
        arr2_row = list(map(int,arr2_cpy[i]))
        temp = ''
        for j in range(n):
            if(arr1_row[j]+arr2_row[j]==0):
                temp += " "
            else:
                temp += "#"
        answer.append(temp)
    return answer

    # def solution(n, arr1, arr2):
    # answer = []
    
    # for i in range(n):
    #     a,b = arr1[i],arr2[i]
    #     c = a|b
    #     ret = 1
    #     temp = ''
    #     for i in range(n-1,-1,-1):
    #         if(c&(ret<<i)):
    #             temp += '#'
    #         else:
    #             temp += " "
    #     answer.append(temp)
    # return answer