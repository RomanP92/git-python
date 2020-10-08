s = input()
a = input()
b = input()
c = 0
while a in s:
    s = s.replace(a, b)
    c += 1
    if c > 1000:
        break
if c <= 1000:
    print(c)
else:
    print('Impossible')