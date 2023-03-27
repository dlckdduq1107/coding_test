
def gcd(a,b):
    while(a%b!=0):
        mod = a%b
        a = b
        b = mod
    return b
        
fchild, dparent = map(int, input().split(" "))

schild, sparent = map(int, input().split(" "))

parent = dparent*sparent
child = fchild*sparent + dparent*schild

gcd_num = gcd(parent, child)
print(child//gcd_num, parent//gcd_num)