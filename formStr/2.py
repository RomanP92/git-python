s = input()
t = input()
c = len(s)
i = 0
j = 0
while i < c-1:
    n = s[i:c]
    if n.startswith(t):
        j += 1
    i += 1
print(j)