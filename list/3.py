my_list = [int(i) for i in input().split()]
my_list1 = []
b = ''
for i in my_list:
    a = my_list.count(i)
    if a > 1 and (my_list1.count(i) < 1):
        my_list1.append(i)
for i in my_list1:
    b += str(i) + ' '
b = b.rstrip()
print(b)