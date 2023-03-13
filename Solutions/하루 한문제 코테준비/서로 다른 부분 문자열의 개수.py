n = input()

sub_set = set()

for i in range(1, len(n)):
    for j in range(len(n)):
        if(j+i <= len(n)):
            sub_set.add(n[j:j+i])

print(len(sub_set)+1)
