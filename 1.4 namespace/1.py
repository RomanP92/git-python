n = int(input())
i = 0
d ={'global': {'parent': 'none', 'values': []}}
def seach_parent(nsp, val):
    if nsp == 'none':
        print('None')
    elif val in d[nsp]['values']:
        print(nsp)
    else:
        nsp = d[nsp]['parent']
        seach_parent(nsp, val)
while i < n:
    cmd, nsp, val = map(str, input().split())
    i += 1
    if cmd == 'create':
        d[nsp] = {"parent": val, 'values': []}
    elif cmd == 'add':
        d[nsp]['values'].append(val)
    else:
        seach_parent(nsp, val)