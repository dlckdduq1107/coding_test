def addTwoNumbers(l1, l2):
    num1 = ''
    num2 = ''
    for i in range(len(l1)-1,-1,-1):
        num1 += str(l1[i])
        num2 += str(l2[i])
    # print(num1,num2)
    result = str(int(num1) + int(num2))
    res = []
    for i in range(len(result)-1,-1,-1):
        res.append(int(result[i]))
    return res
    



print(addTwoNumbers([2,4,3],[5,6,4]))