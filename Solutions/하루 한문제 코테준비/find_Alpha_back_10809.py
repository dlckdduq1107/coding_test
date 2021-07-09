s = input()

for i in range(26):
    find = s.find(chr(i + 97))
    if find != -1:
        print(find, end=' ')
    else:
        print(find, end=' ')


