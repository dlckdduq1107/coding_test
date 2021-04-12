h,w = map(int, input().split())

if h == 1:
    print(1)
elif h == 2:
    print(min(4,(w+1)//2))
elif h >= 3:
    if w < 7:
        print(min(4,w))
    elif w >= 7:
        print(5+(w-7))
