def checkPrime(num):
    divides = set()
    if(num<3):
        return [False, set([1])]
    for i in range(2, num-1):
        if(num%i == 0):
            divides.add(i)
    if(len(divides)==0):
        return [False,set([1])]
    else:
        return [True,divides]
fchild, dparent = map(int, input().split(" "))

schild, sparent = map(int, input().split(" "))

parent = dparent*sparent
child = fchild*sparent + dparent*schild

fcheck,fset = checkPrime(parent)
scheck, sset = checkPrime(child)

# print(fset, sset)
res_set = fset&sset
target = 1
# print(res_set)
if(len(res_set) != 0):
    for i in list(res_set):
        target *= i

print(child//target, parent//target)