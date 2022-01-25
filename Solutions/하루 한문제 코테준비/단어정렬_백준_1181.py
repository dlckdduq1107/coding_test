n = int(input())
words = []
for i in range(n):
    w = input()
    if(w not in words):
        words.append(w)

words.sort()
words.sort(key=lambda x:len(x))
for i in words:
    print(i)