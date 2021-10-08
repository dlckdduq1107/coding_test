import copy
def rotate(array):
    N = len(array)
    res = copy.deepcopy(array)
    for r in range(N):
        for c in range(N):
            res[c][N-1-r] = array[r][c]
    return res
def check(key,lock):
    N = len(key)
    for r in range(N):
        for c in range(N):
            if(key[r][c]+lock[r][c] !=1):
                return False
            # elif(key[r][c]==0 and lock[r][c]==0):
            #     return False

    return True
def partOfKeyUp(array,num):
    if(num==0):
        return copy.deepcopy(array)
    N = len(array)
    temp = copy.deepcopy(array)
    # print(temp)
    part = []
    if(num<=N):
        for i in range(N-num,N):
            part.append(temp[i])
        for j in range(N-num):
            part.append([0 for i in range(N)])
    else:
        for j in range(num-N):
            part.append([0 for i in range(N)])
        for i in range(2*N-num):
            part.append(temp[i])

    return part
def partOfKeyLeft(array,num):
    if(num==0):
        return copy.deepcopy(array)
    N = len(array)
    temp = rotate(array)
    # print(temp)
    part = []
    if(num<=N):
        for i in range(N-num,N):
            part.append(temp[i])
        for j in range(N-num):
            part.append([0 for i in range(N)])
    else:
        for j in range(num-N):
            part.append([0 for i in range(N)])
        for i in range(2*N-num):
            part.append(temp[i])

    for i in range(3):
        part = rotate(part)
    return part

def solution(key, lock):
    # if(check([[0 for i in range(len(key))] for j in range(len(key))], lock)):
    #     return False
    tempArray = copy.deepcopy(key)
    # a = 1
    for i in range(4):
        for j in range(1,len(key)+3):
            k = partOfKeyUp(tempArray,j)
            for q in range(1,len(key)+3):
                last = partOfKeyLeft(k,q)
                # print(last,a)
                # a+=1
                if(check(last,lock)):
                    # print(last)
                    return True
        tempArray = rotate(tempArray)


    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
# print(check([[1,1,1],[1,1,1],[1,1,1]], [[0,0,0],[0,0,0],[0,0,0]]))