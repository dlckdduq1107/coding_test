a,b = input().split(" ")
a = list(a)
a.reverse()

b = list(b)
b.reverse()

# print(a)
a = ''.join(a)
b = ''.join(b)

print(max(int(a),int(b)))
