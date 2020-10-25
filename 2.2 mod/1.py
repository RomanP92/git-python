import datetime
year, month, day = map(int,input().split())
days = int(input())
old = datetime.date(year, month, day) + datetime.timedelta(days)
print(old.year, old.month, old.day)