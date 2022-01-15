s = input()

obj = {}
pivot = 2
count = 0
limit = 3
for i in range(26):
    if(pivot==7 or pivot==9):
        limit=4
    else:
        limit=3
    obj[chr(i+65)] = pivot
    count += 1
    if(count==limit):
        count = 0
        pivot += 1

result = 0
for i in s:
    result += obj[i]+1
print(result)