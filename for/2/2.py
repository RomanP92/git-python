a = int(input())
b = int(input())
c = int(input())
d = int(input())
for j in range(c, d+1):
    print('\t', j, end='')
print('')
for i in range(a, b+1):
    print(i, '\t', end='')
    for a in range(c, d+1):
        print(i * a, '\t', end='')
    print('')