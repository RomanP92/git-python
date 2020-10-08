list_1 = [int(i) for i in input().split()]
y = 0
j = len(list_1)-1
b = ''
if len(list_1) == 1:
    print(list_1[0])
else:
    for i in list_1:
        i = list_1[y+1] + list_1[y-1]
        y += 1
        if y == j:
            y = -1
        b += str(i) + ' '
print(b)