import datetime
d = datetime.datetime(2014,4,2)+datetime.timedelta(days=int(input())-1)
y = str(d.year)
m = str(d.month)
d = str(d.day)
m = '0'*(2-len(m))+m
d = '0'*(2-len(d))+d
print(f"{y}-{m}-{d}")