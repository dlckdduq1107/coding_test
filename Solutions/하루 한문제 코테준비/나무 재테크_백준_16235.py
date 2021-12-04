import copy
def cycle():
    death = []
    for x,rows in enumerate(trees):
        for y,tree in enumerate(rows):
            tree.sort()
            temp = copy.deepcopy(tree)
            for z,each in enumerate(tree):
                lastEnergy = energy[x][y]-each
                if(lastEnergy<0):
                    temp.remove(each)
                    death.append((x,y,each))
                else:
                    energy[x][y]  = lastEnergy
            trees[x][y] = temp

    for x,y,age in death:
        energy[x][y] += age//2

    addTree = []
    for x,rows in enumerate(trees):
        for y,tree in enumerate(rows):
            for z,each in enumerate(tree):
                if(each%5==0):
                    addTree.append((x,y))
    for x,y, in addTree:
        for i in range(8):
            nx,ny = x+dx[i],y+dy[i]
            if(0<=nx<n and 0<+ny<n):
                trees[nx][ny].insert(0,1)

    for i,energyList in enumerate(addEnergy):
        for j,e in enumerate(energyList):
            energy[i][j] += e


    for x,rows in enumerate(trees):
        for y,tree in enumerate(rows):
            for z,each in enumerate(tree):
                trees[x][y][z] += 1

def checkAlive():
    res = 0
    for i in trees:
        for j in i:
           res += len(j)
    return res

dx,dy = [-1,0,1,-1,1,1,1,1],[-1,-1,-1,0,0,-1,0,1]
n,m,k = map(int,input().split(" "))
addEnergy = []
trees = [[[] for i in range(n)] for j in range(n)]
energy = [[5 for i in range(n)] for j in range(n)]
for i in range(n):
    addEnergy.append(list(map(int,input().split(" "))))

for i in range(m):
    x,y,age = map(int,input().split(" "))
    trees[x-1][y-1].append(age)

for i in range(k):
    cycle()

print(checkAlive())

# nxn의땅 모든 땅에는 처음 양분이 5만큼 있다.
# m개의 나무를 처음에 심는다.
# 봄 - 자신의 나이만큼 양분을 먹음, 나이+1, 나무여러개이면 어린나무부터 먹음, 양분 부족하면 그 나무는 바로 죽음
# 여름 - 죽은 나무가 양분이 됨(죽은나무 나이//2)
# 가을 - 나이가 5의배수인 나무가 번식하여 인접 8칸에 나이가 1인 나무가 생김
# 겨율 - addEnergey에 있는 만큼 양분을 추가한다.

