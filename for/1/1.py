a = int(input())
b = int(input())
s = 0
j = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        s += i
        j += 1
print(s / j)