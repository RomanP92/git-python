my_list = [i for i in input().lower().split()]
print(my_list)
d = dict()
s = 1
for i in my_list:
    if i not in d:
        d[i] = s
    else:
        d[i] = d[i] + 1
for key, value in d.items():
    print(key, value)