ppap = input()

if(len(ppap)%3!=1):
    print("NP")
    exit(0)
while('PPAP' in ppap):
    ppap = ppap.replace("PPAP","P")

if(ppap != "P"):
    print("NP")
else:
    print("PPAP")