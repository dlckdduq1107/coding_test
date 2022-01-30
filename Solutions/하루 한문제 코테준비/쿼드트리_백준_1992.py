def quad(arr):
    result=[]
    total = sum([sum(i) for i in arr])
    if(total==len(arr)**2):
        print(1,end='')
    elif(total==0):
        print(0,end='')
    else:
        print('(',end='')
        quad([i[:len(arr)//2] for i in arr[:len(arr)//2]])
        quad([i[len(arr)//2:] for i in arr[:len(arr)//2]])
        quad([i[:len(arr)//2] for i in arr[len(arr)//2:]])
        quad([i[len(arr)//2:] for i in arr[len(arr)//2:]])
        print(')',end='')

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int,list(input()))))

quad(graph)