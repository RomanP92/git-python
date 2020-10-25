a = int(input())
i = 1
d = dict()
while i <= a:
    x = int(input())
    if x not in d:
        d[x] = f(x)
        print(d[x])
        i += 1
    else:
        print(d[x])
        i += 1