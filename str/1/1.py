dnk = input().upper()
cg = dnk.count('C') + dnk.count('G')
lenStr = len(dnk)
perc = cg/lenStr*100
print(perc)