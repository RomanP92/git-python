genome = input()
a = len(genome)
i = 0
j = 1
b = ''
if a == 1:
    print(genome[0]+'1')
while j <= a-1:
    if genome[i] == genome[j]:
        j += 1
    else:
        b += genome[i] + str(j-i)
        i = j
        j += 1
j = a-1
i = a-2
while i >= 0:
    if genome[j] == genome[i]:
        if i == 0:
            b += genome[j] + str(a - i)
        i -= 1
    else:
        b += genome[j] + str(j-i)
        break
print(b)