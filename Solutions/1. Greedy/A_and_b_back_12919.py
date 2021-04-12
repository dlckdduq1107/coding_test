def dfs(string):
    if len(string) == len(end):
        if string == end:
            return 1
        else:
            return 0

    if string[0] == 'B':
        string.reverse()
        del string[-1]
        dfs(string)
        string.append('B')
        string.reverse()

    if string[-1] == 'A':
        del string[-1]
        dfs(string)
        string.append('A')

start = list(input())
end = list(input())

print(dfs(end))

##틀림##