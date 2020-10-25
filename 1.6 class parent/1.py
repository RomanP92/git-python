n = int(input())
i = 0
dct = {}
while i != n:
    a = input()
    if " : " in a:
        clas, parent = map(str, a.split(' : '))
        for j in parent.split():
            if dct.get(j) == None:
                dct[j] = [clas]
            else:
                dct[j].append(clas)
    else:
        clas = str(a)
        parent = 'none'
        dct[parent] = [clas]
    i += 1
q = int(input())
i = 0
while i != q:
    p, c = map(str, input().split())
    def dfs(dct, p):
        visited, stack = [], [p]    
        while stack:        
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)           
                if dct.get(vertex) == None:
                    continue
                else:
                    stack.extend(set(dct[vertex]) - set(visited))
        return visited
    i += 1
    s = (dfs(dct, p))
    if p and c in s:
        print("Yes")
    else:
        print("No")